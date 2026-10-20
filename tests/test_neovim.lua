vim.o.background = "dark"
vim.cmd.colorscheme("xcode_pitch")
assert(vim.g.colors_name == "xcode_pitch")
assert(vim.api.nvim_get_hl(0, { name = "Normal" }).bg == 0x000000)
assert(vim.api.nvim_get_hl(0, { name = "@keyword" }).fg == 0xff7ab2)
vim.o.background = "light"
vim.cmd.colorscheme("xcode_pitch")
assert(vim.api.nvim_get_hl(0, { name = "Normal" }).bg == 0xffffff)
assert(vim.api.nvim_get_hl(0, { name = "@keyword" }).fg == 0xa62169)
assert(vim.g.terminal_color_1 == "#b42318")
print("Standalone Neovim Dark/Light OK (no dotfiles required)")
