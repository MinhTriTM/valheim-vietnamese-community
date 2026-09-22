$ErrorActionPreference = "Continue"
$repoRoot = "E:\SteamLibrary\steamapps\common\valheim-vietnamese-community"
$modsDir = Join-Path $repoRoot "mods"
$outDir = Join-Path $repoRoot "local\extracted_mods"
New-Item -ItemType Directory -Path $outDir -Force | Out-Null

$dllFiles = Get-ChildItem -Path $modsDir -Recurse -Filter "*.dll"
Write-Host "Dang quet $($dllFiles.Count) tap tin DLL..."

foreach ($dll in $dllFiles) {
    try {
        $bytes = [System.IO.File]::ReadAllBytes($dll.FullName)
        $asm = [System.Reflection.Assembly]::Load($bytes)
        $resNames = $asm.GetManifestResourceNames()
        
        $targets = $resNames | Where-Object { 
            $_ -match "\.(json|ya?ml|txt|lang|csv)$" -or 
            $_ -match "(English|localizations|translations|Languages)" 
        }

        if ($targets) {
            $modFolder = $dll.Directory.Name
            $targetModOut = Join-Path $outDir $modFolder
            New-Item -ItemType Directory -Path $targetModOut -Force | Out-Null
            
            foreach ($res in $targets) {
                try {
                    $stream = $asm.GetManifestResourceStream($res)
                    if ($stream) {
                        $reader = New-Object System.IO.StreamReader($stream, [System.Text.Encoding]::UTF8)
                        $content = $reader.ReadToEnd()
                        $reader.Close()
                        $stream.Close()
                        
                        $safeName = $res -replace '[\\/:*?"<>|]', '_'
                        $outFile = Join-Path $targetModOut $safeName
                        [System.IO.File]::WriteAllText($outFile, $content, [System.Text.Encoding]::UTF8)
                        Write-Host "  -> Trich xuat [$modFolder]: $res ($($content.Length) chars)"
                    }
                } catch {
                    Write-Host "    Loi doc resource $($res): $_"
                }
            }
        }
    } catch {
        # Bo qua assembly khong ho tro Load
    }
}

Write-Host "Hoan tat trich xuat manifest resources vao $outDir"
