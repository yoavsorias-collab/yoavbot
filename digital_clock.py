#!/usr/bin/env python3
"""
Digital Clock Application
Display current time in different time zones
"""

import os
import sys
import time
from datetime import datetime
import pytz
from typing import List, Dict, Optional

class DigitalClock:
    """Digital Clock with Multiple Time Zones Support"""
    
    # Popular time zones
    POPULAR_TIMEZONES = {
        '1': ('America/New_York', 'New York (EST/EDT)'),
        '2': ('America/Los_Angeles', 'Los Angeles (PST/PDT)'),
        '3': ('America/Chicago', 'Chicago (CST/CDT)'),
        '4': ('Europe/London', 'London (GMT/BST)'),
        '5': ('Europe/Paris', 'Paris (CET/CEST)'),
        '6': ('Europe/Berlin', 'Berlin (CET/CEST)'),
        '7': ('Europe/Moscow', 'Moscow (MSK)'),
        '8': ('Asia/Tokyo', 'Tokyo (JST)'),
        '9': ('Asia/Shanghai', 'Shanghai (CST)'),
        '10': ('Asia/Hong_Kong', 'Hong Kong (HKT)'),
        '11': ('Asia/Singapore', 'Singapore (SGT)'),
        '12': ('Asia/Dubai', 'Dubai (GST)'),
        '13': ('Asia/Kolkata', 'India (IST)'),
        '14': ('Australia/Sydney', 'Sydney (AEDT/AEST)'),
        '15': ('Pacific/Auckland', 'New Zealand (NZDT/NZST)'),
        '16': ('Asia/Bangkok', 'Bangkok (ICT)'),
        '17': ('Asia/Seoul', 'Seoul (KST)'),
        '18': ('America/Toronto', 'Toronto (EST/EDT)'),
        '19': ('America/Mexico_City', 'Mexico City (CST/CDT)'),
        '20': ('America/Sao_Paulo', 'São Paulo (BRT/BRST)'),
    }
    
    def __init__(self):
        self.selected_zones: List[str] = []
        self.running = True
        self.auto_refresh = False
        self.refresh_interval = 1  # seconds
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        """Print welcome banner"""
        banner = """
╔════════════════════════════════════════════════════════╗
║                                                        ║
║         🕐 DIGITAL CLOCK - MULTIPLE TIME ZONES 🕐     ║
║                                                        ║
╚════════════════════════════���═══════════════════════════╝
        """
        print(banner)
    
    def print_main_menu(self):
        """Print main menu"""
        menu = """
┌──────────────────────────────────────────────────────┐
│               MAIN MENU - Choose an option            │
├──────────────────────────────────────────────────────┤
│                                                      │
│  1. 🕐 View Current Time (All Selected Zones)      │
│  2. ➕ Add Time Zone                               │
│  3. ➖ Remove Time Zone                            │
│  4. 📍 View All Available Time Zones               │
│  5. 🔄 Auto Refresh Clock (Live Update)            │
│  6. 🌍 Set Default Time Zones                      │
│  7. 🔎 Search Time Zone                            │
│  8. 📊 Time Zone Difference Calculator             │
│  9. ❌ Exit                                         │
│                                                      │
└──────────────────────────────────────────────────────┘
        """
        print(menu)
    
    def print_timezone_list(self):
        """Print available time zones"""
        print("\n" + "="*60)
        print("📍 POPULAR TIME ZONES")
        print("="*60)
        
        for key, (tz, name) in self.POPULAR_TIMEZONES.items():
            print(f"  {key:2s}. {name:35s} ({tz})")
        
        print("="*60)
    
    def get_current_time_in_zone(self, timezone: str) -> Optional[Dict]:
        """Get current time in specified timezone"""
        try:
            tz = pytz.timezone(timezone)
            now = datetime.now(tz)
            
            return {
                'timezone': timezone,
                'time': now,
                'hour': now.strftime('%H'),
                'minute': now.strftime('%M'),
                'second': now.strftime('%S'),
                'time_12h': now.strftime('%I:%M:%S %p'),
                'time_24h': now.strftime('%H:%M:%S'),
                'date': now.strftime('%A, %B %d, %Y'),
                'offset': now.strftime('%z'),
                'tzname': now.tzname(),
            }
        except Exception as e:
            return None
    
    def display_clock_visual(self, time_data: Dict):
        """Display a nice visual clock"""
        hour = int(time_data['hour'])
        minute = int(time_data['minute'])
        
        # Calculate clock position (12-hour format for visual)
        hour_12 = hour % 12
        
        # Simple ASCII clock representation
        clock_art = f"""
        ╔═══════════════════╗
        ║   🕐 {time_data['time_12h']}    ║
        ║                   ║
        ║  {time_data['tzname']:12s}      ║
        ║                   ║
        ║  {time_data['date']}  ║
        ║  UTC {time_data['offset']}          ║
        ╚═══════════════════╝
        """
        return clock_art
    
    def display_all_clocks(self):
        """Display all selected time zone clocks"""
        if not self.selected_zones:
            print("❌ No time zones selected!")
            print("➕ Please add a time zone first.")
            return
        
        print("\n" + "="*70)
        print("🕐 CURRENT TIME IN SELECTED TIME ZONES")
        print("="*70)
        
        for timezone in self.selected_zones:
            time_data = self.get_current_time_in_zone(timezone)
            
            if time_data:
                # Get friendly name
                friendly_name = None
                for key, (tz, name) in self.POPULAR_TIMEZONES.items():
                    if tz == timezone:
                        friendly_name = name
                        break
                
                friendly_name = friendly_name or timezone
                
                print(f"\n📍 {friendly_name}")
                print(f"   🕐 Time: {time_data['time_24h']}")
                print(f"   📅 Date: {time_data['date']}")
                print(f"   UTC Offset: {time_data['offset']}")
        
        print("\n" + "="*70)
    
    def add_timezone(self):
        """Add a time zone"""
        print("\n" + "="*60)
        print("➕ ADD TIME ZONE")
        print("="*60)
        
        self.print_timezone_list()
        
        choice = input("\nEnter timezone number or full timezone name (e.g., Asia/Tokyo): ").strip()
        
        if choice in self.POPULAR_TIMEZONES:
            timezone, name = self.POPULAR_TIMEZONES[choice]
            if timezone not in self.selected_zones:
                self.selected_zones.append(timezone)
                print(f"✅ Added: {name}")
            else:
                print(f"⚠️  {name} already selected!")
        else:
            # Try to validate as timezone
            try:
                tz = pytz.timezone(choice)
                if choice not in self.selected_zones:
                    self.selected_zones.append(choice)
                    print(f"✅ Added: {choice}")
                else:
                    print(f"⚠️  {choice} already selected!")
            except:
                print(f"❌ Invalid timezone: {choice}")
        
        input("\nPress Enter to continue...")
    
    def remove_timezone(self):
        """Remove a time zone"""
        if not self.selected_zones:
            print("❌ No time zones to remove!")
            input("Press Enter to continue...")
            return
        
        print("\n" + "="*60)
        print("➖ REMOVE TIME ZONE")
        print("="*60)
        
        for i, tz in enumerate(self.selected_zones, 1):
            friendly_name = None
            for key, (tz_code, name) in self.POPULAR_TIMEZONES.items():
                if tz_code == tz:
                    friendly_name = name
                    break
            
            friendly_name = friendly_name or tz
            print(f"  {i}. {friendly_name}")
        
        try:
            choice = int(input("\nEnter timezone number to remove: "))
            if 1 <= choice <= len(self.selected_zones):
                removed = self.selected_zones.pop(choice - 1)
                print(f"✅ Removed: {removed}")
            else:
                print("❌ Invalid choice!")
        except ValueError:
            print("❌ Invalid input!")
        
        input("Press Enter to continue...")
    
    def set_default_zones(self):
        """Set default time zones"""
        print("\n" + "="*60)
        print("🌍 SET DEFAULT TIME ZONES")
        print("="*60)
        
        print("\nCommon defaults:")
        print("  1. Global (New York, London, Tokyo, Sydney)")
        print("  2. Americas (New York, Chicago, Los Angeles, São Paulo)")
        print("  3. Europe & Asia (London, Paris, Moscow, Tokyo)")
        print("  4. Custom (select your own)")
        
        choice = input("\nChoose default (1-4): ").strip()
        
        defaults = {
            '1': ['America/New_York', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney'],
            '2': ['America/New_York', 'America/Chicago', 'America/Los_Angeles', 'America/Sao_Paulo'],
            '3': ['Europe/London', 'Europe/Paris', 'Europe/Moscow', 'Asia/Tokyo'],
        }
        
        if choice in defaults:
            self.selected_zones = defaults[choice]
            print(f"✅ Default zones set!")
            for tz in self.selected_zones:
                for key, (tz_code, name) in self.POPULAR_TIMEZONES.items():
                    if tz_code == tz:
                        print(f"   • {name}")
                        break
        elif choice == '4':
            self.selected_zones = []
            print("Custom mode - use '➕ Add Time Zone' to add zones")
        else:
            print("❌ Invalid choice!")
        
        input("Press Enter to continue...")
    
    def search_timezone(self):
        """Search for a time zone"""
        print("\n" + "="*60)
        print("🔎 SEARCH TIME ZONE")
        print("="*60)
        
        keyword = input("Enter timezone keyword to search (e.g., 'York', 'Asia'): ").strip().lower()
        
        results = []
        for tz_name in pytz.all_timezones:
            if keyword in tz_name.lower():
                results.append(tz_name)
        
        if results:
            print(f"\n✅ Found {len(results)} timezone(s):")
            for i, tz in enumerate(results[:20], 1):  # Show first 20
                print(f"  {i:2d}. {tz}")
            
            if len(results) > 20:
                print(f"  ... and {len(results) - 20} more")
        else:
            print(f"❌ No timezones found matching '{keyword}'")
        
        input("\nPress Enter to continue...")
    
    def calculate_time_difference(self):
        """Calculate time difference between zones"""
        if len(self.selected_zones) < 2:
            print("❌ Need at least 2 time zones to compare!")
            input("Press Enter to continue...")
            return
        
        print("\n" + "="*60)
        print("📊 TIME ZONE DIFFERENCE CALCULATOR")
        print("="*60)
        
        # Get times in all zones
        times = {}
        for tz in self.selected_zones:
            times[tz] = self.get_current_time_in_zone(tz)
        
        # Calculate differences
        print("\n⏱️  Time Differences:")
        
        utc_now = datetime.now(pytz.UTC)
        
        for tz, time_data in times.items():
            if time_data:
                offset = time_data['offset']
                # Extract offset hours and minutes
                sign = offset[0]
                hours = int(offset[1:3])
                minutes = int(offset[3:5])
                
                # Get friendly name
                friendly_name = None
                for key, (tz_code, name) in self.POPULAR_TIMEZONES.items():
                    if tz_code == tz:
                        friendly_name = name
                        break
                
                friendly_name = friendly_name or tz
                
                print(f"\n  {friendly_name}")
                print(f"    UTC Offset: {offset}")
                print(f"    Current Time: {time_data['time_24h']}")
        
        print("\n" + "="*60)
        input("Press Enter to continue...")
    
    def auto_refresh_clock(self):
        """Auto refresh clock display"""
        print("\n" + "="*60)
        print("🔄 AUTO REFRESH CLOCK")
        print("="*60)
        
        print("\nRefresh Interval Options:")
        print("  1. 1 second (smooth)")
        print("  2. 5 seconds")
        print("  3. 10 seconds")
        
        interval_choice = input("\nChoose interval (1-3): ").strip()
        
        intervals = {'1': 1, '2': 5, '3': 10}
        interval = intervals.get(interval_choice, 1)
        
        print(f"\n⏱️  Auto-refreshing every {interval} second(s)...")
        print("Press Ctrl+C to stop\n")
        
        try:
            while True:
                self.clear_screen()
                self.print_banner()
                self.display_all_clocks()
                print(f"\n⏱️  Updating in {interval} seconds... (Press Ctrl+C to exit)")
                time.sleep(interval)
        
        except KeyboardInterrupt:
            print("\n\n✅ Auto-refresh stopped.")
            input("Press Enter to continue...")
    
    def run(self):
        """Main loop"""
        self.clear_screen()
        self.print_banner()
        
        # Set default zones on first run
        if not self.selected_zones:
            self.selected_zones = ['America/New_York', 'Europe/London', 'Asia/Tokyo']
            print("✅ Default time zones loaded!")
            print("   • New York")
            print("   • London")
            print("   • Tokyo\n")
            time.sleep(2)
        
        try:
            while self.running:
                self.clear_screen()
                self.print_banner()
                self.print_main_menu()
                
                choice = input("Enter your choice (1-9): ").strip()
                self.clear_screen()
                self.print_banner()
                
                if choice == '1':
                    self.display_all_clocks()
                    input("\nPress Enter to continue...")
                elif choice == '2':
                    self.add_timezone()
                elif choice == '3':
                    self.remove_timezone()
                elif choice == '4':
                    self.print_timezone_list()
                    input("\nPress Enter to continue...")
                elif choice == '5':
                    self.auto_refresh_clock()
                elif choice == '6':
                    self.set_default_zones()
                elif choice == '7':
                    self.search_timezone()
                elif choice == '8':
                    self.calculate_time_difference()
                elif choice == '9':
                    self.exit_app()
                else:
                    print("❌ Invalid choice! Please enter 1-9.")
                    input("Press Enter to continue...")
        
        except KeyboardInterrupt:
            print("\n\n⏹️  Application interrupted by user.")
            self.exit_app()
        except Exception as e:
            print(f"\n❌ Unexpected error: {str(e)}")
            self.exit_app()
    
    def exit_app(self):
        """Exit application"""
        print("\n" + "="*60)
        print("👋 Thank you for using Digital Clock!")
        print("="*60)
        print(f"\n✨ Selected {len(self.selected_zones)} time zone(s)")
        print("🕐 Goodbye!\n")
        self.running = False

def main():
    """Entry point"""
    try:
        clock = DigitalClock()
        clock.run()
    except Exception as e:
        print(f"\n❌ Fatal error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
