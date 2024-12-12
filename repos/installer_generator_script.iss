[Setup]
AppName=WZ Audio Manager
AppVersion=1.0
DefaultDirName={pf}\WZ Audio Manager
DefaultGroupName=WZ Audio Manager
OutputDir=.\Output
OutputBaseFilename=installer
Compression=lzma
SolidCompression=yes
SetupIconFile=icon.ico  

[Files]
Source: "wzaudiomanager.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "config.ini"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\WZ Audio Manager"; Filename: "{app}\wzaudiomanager.exe"; IconFilename: "\icon.ico"  
Name: "{userdesktop}\WZ Audio Manager"; Filename: "{app}\wzaudiomanager.exe"; IconFilename: "\icon.ico" 

[Registry]
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Uninstall\WZ Audio Manager"; ValueName: "DisplayName"; ValueData: "WZ Audio Manager"; Flags: uninsdeletekey