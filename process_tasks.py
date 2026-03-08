from pathlib import Path
from datetime import datetime
import re

def main():
    print("="*40)
    print("Task Processor")
    print("="*40)
    
    vault = Path.cwd()
    needs = vault / 'Needs_Action'
    done = vault / 'Done'
    dash = vault / 'Dashboard.md'
    
    done.mkdir(exist_ok=True)
    
    files = list(needs.glob('*.md'))
    
    if not files:
        print("\nNo files to process")
        return
    
    print(f"\nProcessing {len(files)} files\n")
    
    high = 0
    med = 0
    low = 0
    flagged = 0
    
    for f in files:
        print(f"[{f.name}]")
        
        text = f.read_text()
        text_lower = text.lower()
        
        # Priority
        if any(w in text_lower for w in ['urgent', 'asap', 'payment', 'invoice']):
            pri = 'HIGH'
            high += 1
        elif any(w in text_lower for w in ['meeting', 'call', 'review']):
            pri = 'MEDIUM'
            med += 1
        else:
            pri = 'LOW'
            low += 1
        
        # Amount
        amt = 0
        match = re.search(r'\$[\d,]+', text)
        if match:
            amt = int(match.group().replace('$','').replace(',',''))
        
        # Flag
        flag = (amt > 500) or ('urgent' in text_lower)
        if flag:
            flagged += 1
        
        print(f"  Priority: {pri}")
        if amt > 0:
            print(f"  Amount: ${amt}")
        if flag:
            print(f"  ⚠️  Flagged")
        
        # Create summary
        ts = datetime.now().strftime('%Y%m%d_%H%M%S')
        summ = done / f"SUMMARY_{f.stem}_{ts}.md"
        
        content = f"""# Summary: {f.name}

Priority: {pri}
Amount: ${amt}
Flagged: {'Yes' if flag else 'No'}
Processed: {datetime.now()}

## Content
{text[:250]}
"""
        summ.write_text(content)
        
        # Move file
        f.rename(done / f.name)
        print(f"  ✓ Done\n")
    
    # Update dashboard
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    entry = f"- [{now}] Processed {len(files)} files: {high} High, {med} Med, {low} Low\n"
    
    if dash.exists():
        d = dash.read_text()
        if "## Recent Activity" in d:
            d = d.replace("## Recent Activity\n", f"## Recent Activity\n{entry}")
        else:
            d += f"\n## Recent Activity\n{entry}"
        dash.write_text(d)
    
    print("="*40)
    print(f"Total: {len(files)}")
    print(f"High: {high} | Med: {med} | Low: {low}")
    print(f"Flagged: {flagged}")
    print("="*40)

if __name__ == "__main__":
    main()