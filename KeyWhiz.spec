# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.win32.versioninfo import VSVersionInfo, FixedFileInfo, StringFileInfo, StringTable, StringStruct, VarFileInfo, VarStruct

version_info = VSVersionInfo(
    ffi=FixedFileInfo(
        filevers=(1, 0, 0, 0),
        prodvers=(1, 0, 0, 0),
        mask=0x3f,
        flags=0x0,
        OS=0x40004,
        fileType=0x1,
        subtype=0x0,
        date=(0, 0)
    ),
    kids=[
        StringFileInfo([StringTable('040904B0', [
            StringStruct('CompanyName', 'CLOUDWERX LAB'),
            StringStruct('FileDescription', 'KeyWiz - Dynamic Keyboard Shortcut Assistant'),
            StringStruct('FileVersion', '1.0.0'),
            StringStruct('InternalName', 'KeyWiz'),
            StringStruct('LegalCopyright', ' 2024 CLOUDWERX LAB. All rights reserved.'),
            StringStruct('OriginalFilename', 'KeyWiz.exe'),
            StringStruct('ProductName', 'KeyWiz'),
            StringStruct('ProductVersion', '1.0.0')])]),
        VarFileInfo([VarStruct('Translation', [1033, 1200])])
    ]
)

a = Analysis(
    ['keywhiz_app.py'],
    pathex=[],
    binaries=[],
    datas=[('shortcuts/*', 'shortcuts'), ('icons/*', 'icons')],
    hiddenimports=['win32gui', 'win32process', 'win32con'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['_tkinter', 'tkinter', 'tcl', 'tk', 'PIL._tkinter_finder'],
    noarchive=False,
    optimize=2,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='KeyWiz',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['app.ico'],
    version=version_info,
    manifest='<assembly manifestVersion="1.0" xmlns="urn:schemas-microsoft-com:asm.v1">\n  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">\n    <security>\n      <requestedPrivileges>\n        <requestedExecutionLevel level="asInvoker" uiAccess="false"/>\n      </requestedPrivileges>\n    </security>\n  </trustInfo>\n  <compatibility xmlns="urn:schemas-microsoft-com:compatibility.v1">\n    <application>\n      <supportedOS Id="{e2011457-1546-43c5-a5fe-008deee3d3f0}"/>\n      <supportedOS Id="{35138b9a-5d96-4fbd-8e2d-a2440225f93a}"/>\n    </application>\n  </compatibility>\n</assembly>',
)
