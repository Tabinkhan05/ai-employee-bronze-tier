
# File Processor Agent Skill

## Skill Identity
- Name: Inbox File Processor
- Version: 1.0 (Bronze Tier)
- Created: March 8, 2026
- Purpose: Autonomous monitoring and intelligent processing of incoming messages

## When to Activate This Skill
Describe the exact trigger conditions:
- When new .txt files appear in Inbox folder
- When files need priority classification
- When content analysis is required
- When dashboard needs updating

## Prerequisites
List everything that must exist before using this skill:
- Folder structure requirements
- Required files (Company_Handbook.md, Dashboard.md)
- Python dependencies
- System requirements

## Detailed Process Flow

### Phase 1: Detection (file_watcher.py)
Document the complete watching logic:
- How monitoring works (5-second intervals)
- What triggers detection
- How .md files are created
- Frontmatter structure
- Error handling

### Phase 2: Analysis (process_tasks.py)
Document the complete processing logic:
- How Company_Handbook.md rules are loaded
- Priority classification algorithm (with exact keywords)
- Dollar amount extraction (regex pattern: $[',\d]+)
- Approval flagging logic (amount > $500 OR "urgent")
- Summary generation format
- File movement process
- Dashboard update mechanism

### Phase 3: Reporting
- How Dashboard.md is updated
- What Recent Activity entries look like
- How logging works

## Priority Classification Logic
Provide the exact decision tree:
```
IF text contains [urgent, asap, payment, invoice, deadline]:
    priority = HIGH
ELIF text contains [meeting, call, review, important]:
    priority = MEDIUM
ELSE:
    priority = LOW

IF amount > $500 OR "urgent" in text:
    requires_approval = TRUE
```

## Input/Output Specifications

### Input Format
What .txt files in Inbox should look like

### Output Format
Exact structure of:
- .md files in Needs_Action (with frontmatter example)
- SUMMARY files in Done (with complete template)
- Dashboard entries (with exact format)

## Examples

Provide 3 complete examples:

### Example 1: High Priority Urgent Payment
Input file content → Processing steps → Expected output

### Example 2: Medium Priority Meeting Request
Input file content → Processing steps → Expected output

### Example 3: Low Priority Newsletter
Input file content → Processing steps → Expected output

## Error Handling & Edge Cases
- Malformed files
- Missing folders
- Empty Needs_Action
- Duplicate files
- Permission errors

## Performance Metrics
- Processing speed per file
- Memory usage
- Scalability limits

## Integration Points
- Obsidian vault structure
- Claude Code potential usage
- Future MCP server integration
- Cron/scheduler integration

## Troubleshooting Guide
Common issues and solutions

## Version History
- v1.0 (2026-03-08): Initial Bronze Tier implementation

## Future Enhancements (Silver/Gold Tier)
What would be added in next tiers
