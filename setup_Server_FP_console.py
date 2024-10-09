import os
from CONSTANT import *


def create_file_version():
    with open(file_version_name, 'w') as out_file:
        srt_version = f'''VSVersionInfo(
 ffi=FixedFileInfo(
   filevers=(0, 0, {app_nr_version_}, {app_nr2_version_}),
   prodvers=(0, 0, {app_nr_version_}, {app_nr2_version_}),
   mask=0x3f,
   flags=0x0,
   OS=0x40004,
   fileType=0x1,
   subtype=0x0,
   date=(0, 0)
   ),
 kids=[
   StringFileInfo(
     [
     StringTable(
       u'040904B0',
       [StringStruct(u'CompanyName', u'{CompanyName_}'),
       StringStruct(u'FileDescription', u'{FileDescription_}'),
       StringStruct(u'FileVersion', u'0.0.{app_nr_version_}.{app_nr2_version_}'),
       StringStruct(u'InternalName', u'{InternalName_}'),
       StringStruct(u'LegalCopyright', u'Unisim-Soft. All rights reserved.'),
       StringStruct(u'OriginalFilename', u'{OriginalFilename_}'),
       StringStruct(u'ProductName', u'{ProductName_}'),
       StringStruct(u'ProductVersion', u'0.0.{app_nr_version_}.{app_nr2_version_}')])
       ]),
   VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
 ]
)'''

        out_file.write(srt_version)


# Just add or remove values to this list based on the imports you don't want : )
excluded_modules = [
    'jedi',
    'psutil',
    'tk',
    'ipython',
    'tcl',
    'tcl8',
    'tornado'
]

app_nr_version_ = version_nr
app_nr2_version_ = app_nr2_version
CompanyName_ = CompanyName
FileDescription_ = FileDescription
InternalName_ = InternalName
OriginalFilename_ = OriginalFilename
ProductName_ = ProductName

file_version_name = 'server_fp_version.py'
create_file_version()

append_string = ''
for mod in excluded_modules:
    append_string += ' --exclude-module {mod}'.format(mod=mod)

# Run the shell command with all the exclude module parameters
os.system(f'pyinstaller -F -i ico.ico '
          f'-n {OriginalFilename_}_console '
          f'Server_FP.py '
          f'--version-file {file_version_name} '
          '--hidden-import=pkg_resources '
          '--hidden-import=pkg_resources.py2_warn '
          '--hidden-import=pkg_resources.extern '
          f'{append_string} '
          )
