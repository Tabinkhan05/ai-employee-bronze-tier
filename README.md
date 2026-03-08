# AI Employee System - Bronze Tier ✅

> A local-first autonomous AI assistant that monitors, analyzes, and processes incoming messages 24/7 using Claude Code and Obsidian.

## 🎯 Overview

This Bronze Tier implementation provides:
- **Continuous monitoring** of Inbox folder
- **Intelligent priority detection** based on keywords and dollar amounts
- **Automated processing** pipeline
- **Human-in-the-loop flagging** for sensitive items
- **Real-time dashboard** updates

## 🏗️ System Architecture
```
┌─────────────────────────────────────────────┐
│          AI EMPLOYEE SYSTEM                 │
│          Bronze Tier v1.0                   │
└─────────────────────────────────────────────┘

   📁 Inbox                    👁️ File Watcher
      ↓                           (Python)
   New .txt files                    ↓
      ↓                       Continuous Monitoring
      ↓                              ↓
   📋 Needs_Action          🧠 Task Processor
      ↓                         (Python)
   Analysis &                       ↓
   Priority Detection        📊 Dashboard Update
      ↓                           (Markdown)
      ↓                              ↓
   ✅ Done Folder               📝 Activity Logs
```

## 🚀 Quick Start

### Prerequisites
- Python 3.13+
- Obsidian (optional, for visual dashboard)
- Basic terminal knowledge

### Installation
```bash
# Clone or navigate to vault
cd AI_employee_vault

# Verify folder structure
ls -la
# Should see: Inbox, Needs_Action, Done, Logs, etc.
```

### Running the System

**Method 1: Manual (Recommended for Bronze)**
```bash
# Terminal 1: Start file watcher
python3 file_watcher.py

# Terminal 2: Drop files in Inbox
cp your_file.txt Inbox/

# Terminal 3: Process tasks
python3 process_tasks.py
```

**Method 2: Automated (Optional)**
```bash
# Start watcher in background
nohup python3 file_watcher.py &

# Schedule processing (add to crontab)
*/15 * * * * cd /path/to/vault && python3 process_tasks.py
```

## 📂 Folder Structure
```
AI_Employee_Vault/
├── Inbox/                 # Drop .txt files here
├── Needs_Action/          # Pending processing (auto-populated)
├── Done/                  # Completed tasks + summaries
├── Logs/                  # Activity logs
├── Skills/                # Agent skill documentation
│   └── file_processor/
│       └── SKILL.md
├── Company_Handbook.md    # Rules & priorities
├── Dashboard.md           # Real-time overview
├── file_watcher.py        # Monitoring script
├── process_tasks.py       # Processing engine
└── README.md              # This file
```

## 💡 How It Works

### Step 1: File Detection
```bash
echo "URGENT: Payment needed" > Inbox/payment.txt
```
→ Watcher detects → Creates `payment_TIMESTAMP.md` in Needs_Action

### Step 2: Processing
```bash
python3 process_tasks.py
```
→ Analyzes content → Assigns priority → Creates summary → Moves to Done

### Step 3: Review
```bash
cat Dashboard.md
```
→ See updated activity → Check flagged items → Review summaries

## 🎨 Features

### ✅ Implemented (Bronze Tier)
- [x] Continuous inbox monitoring (5-second intervals)
- [x] Intelligent priority detection (High/Medium/Low)
- [x] Dollar amount extraction ($500+ flagging)
- [x] Human approval flagging for sensitive items
- [x] Automated dashboard updates
- [x] Comprehensive logging
- [x] Summary generation with metadata

### 🔮 Planned (Silver/Gold Tier)
- [ ] Gmail API integration
- [ ] WhatsApp monitoring
- [ ] MCP servers for actions (send emails, schedule meetings)
- [ ] Real-time Claude Code analysis
- [ ] Multi-domain processing
- [ ] Weekly CEO briefings

## 📊 Priority System

| Priority | Keywords | Threshold | Action |
|----------|----------|-----------|--------|
| 🔴 **HIGH** | urgent, asap, payment, invoice, deadline | Amount > $500 | ⚠️ Flag for approval |
| 🟡 **MEDIUM** | meeting, call, review, important | - | Auto-process |
| 🟢 **LOW** | newsletter, update, fyi | - | Auto-archive |

## 📝 Usage Examples

### Example 1: Urgent Client Request
```bash
cat > Inbox/client_urgent.txt << 'EOF'
From: client@bigcorp.com
Subject: URGENT - Proposal Needed

We need the Q1 proposal ASAP. Budget is $5,000.
Please send by EOD.
EOF
```

**Result:**
- Priority: HIGH
- Amount: $5,000
- Flagged: ⚠️ Yes
- Action: Review and approve

### Example 2: Meeting Request
```bash
echo "Can we schedule a review meeting next week?" > Inbox/meeting.txt
```

**Result:**
- Priority: MEDIUM
- Amount: $0
- Flagged: No
- Action: Auto-process

### Example 3: Newsletter
```bash
echo "FYI - Monthly tech newsletter" > Inbox/newsletter.txt
```

**Result:**
- Priority: LOW
- Amount: $0
- Flagged: No
- Action: Archive

## 🎓 Bronze Tier Achievements

✅ **Core Functionality**
- Obsidian vault with proper structure
- File system watcher (continuous monitoring)
- Claude Code integration potential
- Automated processing pipeline

✅ **Advanced Features**
- Priority detection system
- Dollar amount extraction
- Human approval flagging
- Dashboard auto-updates
- Comprehensive logging

✅ **Documentation**
- Agent skill documentation
- README with examples
- Folder structure guide
- Troubleshooting tips

## 🐛 Troubleshooting

### Issue: Watcher not detecting files
```bash
# Check if watcher is running
ps aux | grep file_watcher

# Check Inbox folder permissions
ls -la Inbox/

# Restart watcher
pkill -f file_watcher
python3 file_watcher.py
```

### Issue: Processing errors
```bash
# Check Python version
python3 --version  # Should be 3.13+

# Test syntax
python3 -m py_compile process_tasks.py

# Check file permissions
chmod +x process_tasks.py
```

### Issue: Dashboard not updating
```bash
# Verify Dashboard.md exists
ls -la Dashboard.md

# Check write permissions
chmod 644 Dashboard.md
```

## 📞 Support

**Wednesday Research Meetings:**
- Time: Every Wednesday 10 PM
- Zoom: https://us06web.zoom.us/j/87188707642
- YouTube: https://www.youtube.com/@panaversity

## 📄 Submission

**Hackathon Submission Form:**
https://forms.gle/JR9T1SJq5rmQyGkGA

**Required:**
- [x] GitHub repository
- [x] README.md (this file)
- [x] Demo video (5-10 minutes)
- [ ] Security disclosure
- [x] Tier declaration: **Bronze**

## 🏆 Next Steps

Ready for **Silver Tier**? Add:
1. Gmail watcher (API integration)
2. MCP server for email actions
3. WhatsApp monitoring
4. Human-in-the-loop approval workflow
5. Multi-watcher coordination

## 📜 License

Built for Panaversity AI Employee Hackathon 2026

---

**Version:** 1.0 (Bronze Tier Complete)  
**Last Updated:** March 8, 2026  
**Status:** ✅ Production Ready
```

---

## 🎬 Create Demo Video

Record a **5-10 minute demo** showing:

1. **System Overview** (30 sec)
   - Show folder structure
   - Explain architecture

2. **File Watcher Demo** (2 min)
   - Start watcher
   - Drop test file in Inbox
   - Show detection in terminal
   - Show .md file created in Needs_Action

3. **Processing Demo** (2 min)
   - Run process_tasks.py
   - Show priority detection
   - Show flagging system
   - Show files moving to Done

4. **Results Review** (2 min)
   - Open Dashboard.md
   - Show summary files
   - Explain priority system
   - Show logs

5. **Complete Flow** (2 min)
   - Drop 3 diverse files
   - Show end-to-end processing
   - Highlight automation

6. **Future Vision** (1 min)
   - Mention Silver tier plans
   - Thank viewers

---

## 🎊 BRONZE TIER COMPLETION CERTIFICATE
```
╔══════════════════════════════════════════════════╗
║                                                  ║
║      🏆 BRONZE TIER COMPLETED 🏆                ║
║                                                  ║
║  AI Employee Hackathon 2026                     ║
║  Panaversity                                     ║
║                                                  ║
║  Developer: Tabin                                ║
║  Date: March 8, 2026                            ║
║                                                  ║
║  Achievements:                                   ║
║  ✅ Vault Structure                             ║
║  ✅ File Watcher                                ║
║  ✅ Task Processor                              ║
║  ✅ Priority Detection                          ║
║  ✅ Dashboard Integration                       ║
║  ✅ Agent Skill Documentation                   ║
║  ✅ Comprehensive README                        ║
║                                                  ║
║  Status: PRODUCTION READY ✅                    ║
║                                                  ║
╚══════════════════════════════════════════════════╝