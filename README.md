```markdown
# Admin Panel Finder Tool

This Python script is designed to help users identify potential admin panels on websites. It does so by checking a list of common admin paths against the provided website URL. The tool utilizes concurrent threading to efficiently scan for these paths and outputs any discovered admin panels.

## Features

- **Custom Admin Directories:** Users can provide their own list of admin directories for scanning.
- **Threaded Requests:** Utilizes concurrent threading to speed up the scanning process.
- **Detailed Results:** Outputs found admin panels with URLs for further investigation.
- **User-Friendly Interface:** Simple prompts guide users through the scanning process.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/admin-panel-finder.git
   ```

2. **Navigate to the Directory:**
   ```bash
   cd admin-panel-finder
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script:**
   ```bash
   python admin_finder.py
   ```

5. **Follow the Prompts:**
   - Enter the website URL when prompted.
   - Optionally, provide a custom admin directories file.
   - Sit back and wait for the scan to complete.

## Custom Admin Directories File

Users have the option to specify their own list of admin directories for scanning. Simply create a text file with one admin directory per line and provide the path to this file when prompted.

## Example:

```plaintext
http://example.com
```

## Notes

- Ensure Python is installed on your system.
- Use the tool responsibly to avoid overwhelming servers with excessive requests.
- Happy admin panel hunting!

```