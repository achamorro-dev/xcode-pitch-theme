local M = {}
local applying = false

-- Public renderer: consumers may supply their own palette without copying the
-- highlight implementation. There is no dependency on personal dotfiles/state.
function M.apply(p, opts)
  if applying then
    return
  end
  applying = true
  opts = opts or {}
  vim.o.termguicolors = true
  vim.o.background = p.mode
  vim.cmd("highlight clear")
  vim.g.colors_name = opts.name or "xcode_pitch"
  local function hl(group, fg, bg, extra)
    vim.api.nvim_set_hl(0, group, vim.tbl_extend("force", { fg = fg, bg = bg }, extra or {}))
  end
  hl("Normal", p.foreground, p.background)
  hl("NormalNC", p.foreground, p.background)
  hl("NormalFloat", p.foreground, p.surface)
  hl("FloatBorder", p.border, p.surface)
  hl("WinSeparator", p.border, p.background)
  hl("SignColumn", nil, p.background)
  hl("LineNr", p.muted, p.background)
  hl("CursorLineNr", p.foreground, p.background, { bold = true })
  hl("CursorLine", nil, p.surface)
  hl("Cursor", p.background, p.cursor)
  hl("Visual", nil, p.selection)
  hl("Search", p.background, p.yellow)
  hl("IncSearch", p.background, p.orange)
  hl("MatchParen", p.accent, p.raised, { bold = true })
  hl("NonText", p.muted)
  hl("Whitespace", p.border)
  hl("Pmenu", p.foreground, p.surface)
  hl("PmenuSel", p.foreground, p.selection)
  hl("StatusLine", p.foreground, p.surface)
  hl("StatusLineNC", p.muted, p.background)
  hl("TabLine", p.muted, p.surface)
  hl("TabLineSel", p.accent, p.background, { bold = true })
  hl("TabLineFill", nil, p.background)
  hl("Folded", p.muted, p.surface)
  hl("Title", p.accent, nil, { bold = true })
  hl("Directory", p.blue)
  hl("ErrorMsg", p.red)
  hl("WarningMsg", p.yellow)
  for group, role in pairs({
    Comment = "comment", Constant = "number", String = "string", Character = "string",
    Number = "number", Boolean = "number", Float = "number", Identifier = "variable",
    Function = "function", Statement = "keyword", Conditional = "keyword", Repeat = "keyword",
    Label = "keyword", Operator = "operator", Keyword = "keyword", Exception = "keyword",
    PreProc = "orange", Include = "keyword", Define = "keyword", Type = "type",
    StorageClass = "keyword", Structure = "type", Typedef = "type", Special = "cyan",
    Delimiter = "punctuation", SpecialComment = "comment", Underlined = "blue",
    ["@comment"] = "comment", ["@string"] = "string", ["@number"] = "number",
    ["@boolean"] = "number", ["@constant"] = "number", ["@variable"] = "variable",
    ["@variable.parameter"] = "cyan", ["@variable.member"] = "cyan",
    ["@function"] = "function", ["@function.call"] = "purple", ["@function.method"] = "function",
    ["@keyword"] = "keyword", ["@type"] = "type", ["@type.builtin"] = "purple",
    ["@operator"] = "operator", ["@punctuation"] = "punctuation", ["@tag"] = "keyword",
    ["@tag.attribute"] = "purple", ["@module"] = "variable",
    ["@lsp.type.variable"] = "variable", ["@lsp.type.parameter"] = "cyan",
    ["@lsp.type.property"] = "cyan", ["@lsp.type.function"] = "function",
    ["@lsp.type.method"] = "function", ["@lsp.type.class"] = "type",
    ["@lsp.type.interface"] = "type", ["@lsp.type.enum"] = "type",
    ["@markup.heading"] = "accent", ["@markup.link"] = "blue", ["@markup.raw"] = "string",
  }) do
    hl(group, p[role], nil, { bold = role == "keyword" })
  end
  for suffix, color in pairs({ Error = p.red, Warn = p.yellow, Info = p.blue, Hint = p.cyan }) do
    hl("Diagnostic" .. suffix, color)
    hl("DiagnosticUnderline" .. suffix, nil, nil, { undercurl = true, sp = color })
  end
  hl("DiffAdd", p.green, p.surface)
  hl("DiffDelete", p.red, p.surface)
  hl("DiffChange", p.blue, p.surface)
  hl("DiffText", p.foreground, p.selection)
  hl("GitSignsAdd", p.green)
  hl("GitSignsChange", p.blue)
  hl("GitSignsDelete", p.red)
  local ansi = { p.black, p.red, p.green, p.yellow,
    p.blue, p.purple, p.cyan, p.white, p.muted, p.red, p.green, p.yellow,
    p.blue, p.purple, p.cyan, p.brightWhite }
  for i, color in ipairs(ansi) do
    vim.g["terminal_color_" .. (i - 1)] = color
  end
  applying = false
end

function M.load()
  M.apply(require("xcode_pitch.palettes")[vim.o.background])
end

return M
