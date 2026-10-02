-- Neudata revealjs filters
--  * Level-1 headings (# Section) become section dividers with the logo and a
--    teal rule, as in the Beamer and PowerPoint templates.
--  * A closing copyright slide is appended. Turn it off with `copyright-slide: false`.

local COPYRIGHT_PARAS = {
  "All property rights and copyright are reserved.",
  "This presentation contains proprietary data, information, and materials developed by Neudata for " ..
    "dedicated use only and may not be communicated, copied, reproduced, distributed, published, or " ..
    "cited, in whole or in part, without the prior written consent of Neudata. Where explicit written " ..
    "permission has been granted, appropriate attribution must be included, followed by " ..
    "\u{201C}by courtesy of Neudata\u{201D}.",
  "Any unauthorized use or infringement of these materials may give rise to legal action and claims " ..
    "for damages, without prejudice to any other rights of Neudata, including rights relating to " ..
    "patents, trademarks, or other forms of intellectual property protection.",
}

local function html_escape(s)
  return (s:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;"))
end

local section_count = 0
local section_label = "Section"   -- override with `section-label:` in the front matter (e.g. "Phần")

local function read_meta(meta)
  if meta["section-label"] ~= nil then
    section_label = pandoc.utils.stringify(meta["section-label"])
  end
end

local function section_header(el)
  if not quarto.doc.is_format("revealjs") or el.level ~= 1 then
    return nil
  end
  section_count = section_count + 1
  el.classes:insert("neudata-section")
  el.attributes["data-section-number"] = tostring(section_count)
  return {
    el,
    pandoc.RawBlock("html",
      '<div class="neudata-section-art">' ..
      '<img class="neudata-section-logo" src="neudata-logo.png" alt="">' ..
      '<span class="neudata-section-rule"></span>' ..
      '</div>' ..
      '<p class="neudata-section-number">' .. section_label .. ' ' .. section_count .. '</p>'),
  }
end

local function copyright_slide(doc)
  if not quarto.doc.is_format("revealjs") then
    return doc
  end
  local cs = doc.meta["copyright-slide"]
  local off = (cs == false) or (cs ~= nil and pandoc.utils.stringify(cs) == "false")
  if off then
    return doc
  end
  local paras = {}
  for _, p in ipairs(COPYRIGHT_PARAS) do
    table.insert(paras, "<p>" .. html_escape(p) .. "</p>")
  end
  doc.blocks:insert(pandoc.Header(2, {}, pandoc.Attr("neudata-copyright", { "neudata-copyright-slide" })))
  doc.blocks:insert(pandoc.RawBlock("html",
    '<img class="neudata-copyright-logo" src="neudata-logo.png" alt="Neudata Consulting Ltd">' ..
    '<p class="neudata-copyright-title">Copyright \u{00A9} Neudata, ' .. os.date("%Y") .. '</p>' ..
    '<div class="neudata-copyright-text">' .. table.concat(paras) .. '</div>'))
  return doc
end

-- Run in order: read metadata first, then number the sections, then add the closing slide
return {
  { Meta = function(meta) read_meta(meta) end },
  { Header = section_header },
  { Pandoc = copyright_slide },
}
