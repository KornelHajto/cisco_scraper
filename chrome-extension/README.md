# Cisco Questions Search Overlay Extension

A powerful Chrome extension that provides a **transparent overlay** for searching through Cisco exam questions. Activated with a simple keyboard shortcut, it appears on top of any webpage with a glassmorphic design.

## 🚀 Features

### ⌨️ **Keyboard-Activated Overlay**
- **Global shortcut**: `Ctrl+Shift+Q` (or `Cmd+Shift+Q` on Mac)
- **Works on any webpage** - no need to open a popup
- **Transparent glassmorphic design** with backdrop blur
- **ESC key to close** or click outside to dismiss

### 🔍 **Advanced Search**
- **Real-time search** as you type
- Search across question text, options, correct answers, and explanations
- **Case-insensitive** matching with **highlighted results**
- Search by question number or keywords
- **Instant results** - no loading delays

### 📋 **Beautiful Question Display**
- **Glassmorphic cards** with smooth animations
- Color-coded sections:
  - 🟦 Questions with transparent blue headers
  - 🟩 Correct answers highlighted in green
  - 🟨 Search terms highlighted in yellow
  - 💡 Explanations in dedicated info boxes

### ✨ **User Experience**
- **Slide-down animation** when opening
- **Fade effects** and smooth transitions
- **Auto-focus** on search field
- **Responsive design** - works on mobile and desktop
- **Custom scrollbars** with glassmorphic styling

## 📸 Preview

```
┌─────────────────────────────────────────┐
│  🔍 Cisco Questions Search              ×│
├─────────────────────────────────────────┤
│  [Search questions, answers...    ] 🔍 │
│                                   Clear │
├─────────────────────────────────────────┤
│  📊 25 of 150 questions found           │
├─────────────────────────────────────────┤
│  ┌─ Question 1 ─────────── [multiple]┐  │
│  │  Which statement describes ASA...  │  │
│  │  📝 Options:                      │  │
│  │     • ASA uses ? command...       │  │
│  │     • To use show command...      │  │
│  │  ✅ Correct: To use show command...│  │
│  │  💡 Explanation: The ASA CLI...   │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

## 🛠 Installation

### Quick Install (Recommended)

1. **Open Chrome** → Navigate to `chrome://extensions/`
2. **Enable Developer mode** (toggle in top-right)
3. **Click "Load unpacked"**
4. **Select folder**: `C:\Users\Kornel Hajto\Documents\scraper_cisco\chrome-extension\`
5. **Done!** The extension is now active

### With Custom Icons (Optional)

1. **Generate icons**: Double-click `generate_icons.bat`
2. **Download icons**: Follow the web page instructions
3. **Save as**: `icon16.png`, `icon48.png`, `icon128.png` in `icons/` folder
4. **Install**: Follow Quick Install steps above

## ⌨️ How to Use

### Opening the Overlay
- **Keyboard shortcut**: `Ctrl+Shift+Q` (Windows/Linux) or `Cmd+Shift+Q` (Mac)
- Works on **any webpage** - no need to navigate anywhere special

### Searching
- **Type immediately** - search field is auto-focused
- **Real-time results** appear as you type
- **Press Enter** to search or **ESC** to close

### Closing the Overlay
- **ESC key** - Quick close
- **Click outside** the overlay
- **× button** in top-right corner
- **Keyboard shortcut again** - toggles on/off

## 🎯 Search Examples

| Search Type | Example | Finds |
|-------------|---------|-------|
| **Question Number** | `1`, `2`, `15` | Specific question by number |
| **Technology** | `ASA`, `CLI`, `router` | Questions about specific topics |
| **Commands** | `show`, `access-list` | Configuration-related questions |
| **Answers** | `extended access` | Questions with specific answers |
| **Explanations** | `configuration mode` | Questions with detailed explanations |

## 📁 File Structure

```
chrome-extension/
├── 📄 manifest.json              # Extension configuration (Manifest V3)
├── 🎨 overlay.css               # Glassmorphic styling & animations
├── 🧠 content.js                # Overlay logic & search functionality  
├── ⚙️  background.js             # Keyboard shortcuts & communication
├── 📊 extracted_questions.json  # Your questions database
├── 🖼️  icons/                   # Extension icons
│   ├── icon16.png
│   ├── icon48.png
│   └── icon128.png
├── 🎨 create_icons.html         # Icon generator utility
├── 📋 generate_icons.bat        # Quick icon generation script
└── 📖 README.md                 # This documentation
```

## 🔧 Technical Details

### Architecture
- **Manifest V3** - Latest Chrome extension standard
- **Content Scripts** - Injected into all web pages
- **Background Service Worker** - Handles keyboard commands
- **Overlay System** - Transparent glassmorphic UI

### Performance
- **Lightweight**: < 50KB total size
- **Fast loading**: Questions cached after first load
- **Smooth animations**: CSS transforms with GPU acceleration
- **Memory efficient**: Only active when overlay is visible

### Permissions
- `activeTab` - To inject content scripts
- `storage` - For future preferences (unused currently)

### Keyboard Shortcuts
- **Primary**: `Ctrl+Shift+Q` / `Cmd+Shift+Q`
- **Secondary**: `ESC` to close
- **Customizable** via Chrome's keyboard shortcuts settings

## 🎨 Customization

### Change Colors
Edit `overlay.css`:
```css
/* Primary brand color */
--cisco-blue: #1f5582;

/* Glassmorphic background */
--glass-bg: rgba(255, 255, 255, 0.95);

/* Highlight color */
--highlight-color: #ffeb3b;
```

### Modify Keyboard Shortcut
1. Go to `chrome://extensions/shortcuts`
2. Find "Cisco Questions Search Overlay"
3. Click pencil icon and set new shortcut

### Update Questions Database
1. Replace `extracted_questions.json` with new file
2. Reload extension: `chrome://extensions/` → ⟳ button
3. Questions automatically update

## 🔍 Question Data Format

Expected JSON structure:
```json
[
  {
    "question_number": "1",
    "question_text": "Which statement describes...",
    "options": [
      "Option A text",
      "Option B text",  
      "Option C text"
    ],
    "correct_answers": ["Option B text"],
    "type": "multiple_choice",
    "explanation": "Detailed explanation here..."
  }
]
```

### Supported Question Types
- `multiple_choice` - Single or multiple correct answers
- `matching` - Match items between columns
- `true_false` - True/False questions
- `fill_blank` - Fill in the blank
- Custom types display as badges

## 🌐 Browser Compatibility

| Browser | Support | Notes |
|---------|---------|-------|
| **Chrome** | ✅ 88+ | Full support (recommended) |
| **Edge** | ✅ 88+ | Full support |
| **Firefox** | ❌ | Different extension API |
| **Safari** | ❌ | Different extension system |

## 🚨 Troubleshooting

### Overlay Not Appearing
1. **Check shortcut**: Try `Ctrl+Shift+Q` on any webpage
2. **Reload extension**: `chrome://extensions/` → ⟳ button
3. **Check permissions**: Ensure extension is enabled
4. **Console errors**: F12 → Console tab for error messages

### Search Not Working  
1. **Verify data**: Open `extracted_questions.json` - should be valid JSON
2. **Clear search**: Click "Clear" button and try again
3. **Check file size**: Large files (>10MB) may load slowly
4. **Reload page**: F5 to reinitialize extension

### Performance Issues
1. **Too many results**: Search returns 20 max - be more specific
2. **Large dataset**: Consider splitting questions into smaller files
3. **Memory usage**: Close other tabs to free up resources

### Keyboard Shortcut Conflicts
1. **Change shortcut**: `chrome://extensions/shortcuts`
2. **Check conflicts**: Other extensions may use same keys
3. **Alternative**: Use ESC to close overlay

## 🔄 Updates & Maintenance

### Updating Questions
1. Export new `extracted_questions.json` from your scraper
2. Replace file in extension folder
3. Reload extension or restart Chrome

### Version Updates
- Extension auto-updates if installed from Chrome Web Store
- For development: manually reload in `chrome://extensions/`

### Backup Settings
- Questions file: Back up `extracted_questions.json`
- Custom shortcuts: Note changes in Chrome shortcuts settings

## 🤝 Contributing

### Development Setup
1. Clone/download extension folder
2. Load unpacked in Chrome
3. Make changes to source files
4. Reload extension to test

### Reporting Issues
- Check console for JavaScript errors
- Note Chrome version and OS
- Describe steps to reproduce
- Include sample question data if relevant

### Feature Requests
- Search enhancements
- UI/UX improvements  
- Additional question types
- Export/import functionality

## 📄 License

This extension is provided as-is for educational purposes. Ensure you have proper rights to use any question content in your `extracted_questions.json` file.

---

**Happy studying! 🎓**

*Press `Ctrl+Shift+Q` on any webpage to start searching your Cisco questions instantly.*