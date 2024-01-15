# Specify the path to the folder you want to delete
$folderPath = "C:\Users\patil\Desktop\SIH Project\Ctrl-Alt-Defeat\client\runs"

# Check if the folder exists
if (Test-Path -Path $folderPath -PathType Container) {
    try {
        # Forcefully remove the folder and its contents
        Remove-Item -Path $folderPath -Recurse -Force -ErrorAction Stop
        Write-Host "Folder '$folderPath' and its contents deleted successfully."
    } catch {
        Write-Host "Error: $_"
    }
} else {
    Write-Host "Folder '$folderPath' does not exist."
}

python main.py