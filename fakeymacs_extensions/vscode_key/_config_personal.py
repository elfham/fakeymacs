﻿# -*- mode: python; coding: utf-8-with-signature-dos -*-

# 本ファイルは、config_personal.py というファイル名にすることで vscode_key Extension の
# 機能拡張ファイルとして機能します。以下はサンプルコードです。

def toggle_editor_layout():
    # VSCode Command : Toggle Vertical/Horizontal Editor Layout
    self_insert_command("A-S-0")()
    # vscodeExecuteCommand("workbench.action.toggleEditorGroupLayout")()

define_key3(keymap_emacs, "Ctl-x 4", toggle_editor_layout)
