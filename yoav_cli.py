#!/usr/bin/env python3
"""
Yoav Bot - CLI (Command Line Interface)
Run directly in terminal - No Discord needed!
"""

import os
import sys
from datetime import datetime
from minecraft_helper import MinecraftModGenerator
from ai_engine import YoavAIEngine

class YoavBotCLI:
    """Yoav Bot Command Line Interface"""
    
    def __init__(self):
        self.bot_name = "🤖 Yoav Bot"
        self.version = "1.0.0"
        self.mod_generator = MinecraftModGenerator()
        self.ai_engine = YoavAIEngine()
        self.running = True
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        """Print welcome banner"""
        banner = """
╔════════════════════════════════════════════════════════╗
║                                                        ║
║           🤖 YOAV BOT - CLI INTERFACE 🤖             ║
║                  Version 1.0.0                        ║
║                                                        ║
║        Your AI Assistant for Minecraft & Coding       ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
        """
        print(banner)
    
    def print_menu(self):
        """Print main menu"""
        menu = """
┌─────────────────────────────────────────────────────┐
│              MAIN MENU - Choose an option            │
├─────────────────────────────────────────────────────┤
│                                                     │
│  1. 🎮  Create Minecraft Mod                       │
│  2. 🎨  Generate Image (Text Description)         │
│  3. 🔊  Text to Speech (Convert text to audio)    │
│  4. 💻  Generate Code (Python/Java/JavaScript)    │
│  5. ℹ️   Bot Information                           │
│  6. 📋  Help & Commands                           │
│  7. ❌  Exit                                       │
│                                                     │
└─────────────────────────────────────────────────────┘
        """
        print(menu)
    
    def create_minecraft_mod(self):
        """Create a Minecraft mod"""
        print("\n" + "="*50)
        print("🎮 MINECRAFT MOD GENERATOR")
        print("="*50)
        
        print("\nMod Types:")
        print("  1. Basic Mod")
        print("  2. Tool Mod")
        print("  3. Block Mod")
        print("  4. Entity Mod")
        
        try:
            mod_type_choice = input("\nChoose mod type (1-4): ").strip()
            
            mod_types = {
                '1': 'basic',
                '2': 'tool',
                '3': 'block',
                '4': 'entity'
            }
            
            mod_type = mod_types.get(mod_type_choice, 'basic')
            mod_name = input("Enter mod name: ").strip()
            
            if not mod_name:
                mod_name = "MyAwesomeMod"
            
            print(f"\n⏳ Generating {mod_type} mod '{mod_name}'...")
            
            mod_code = self.mod_generator.generate_mod(mod_type, mod_name)
            
            print("\n✅ Mod Generated Successfully!")
            print("\n" + "="*50)
            print("MOD CODE:")
            print("="*50)
            print(mod_code)
            print("="*50)
            
            # Save to file
            filename = f"mods/{mod_name}_{mod_type}.java"
            os.makedirs("mods", exist_ok=True)
            
            with open(filename, 'w') as f:
                f.write(mod_code)
            
            print(f"\n💾 Mod saved to: {filename}")
            
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def generate_image(self):
        """Generate image from description"""
        print("\n" + "="*50)
        print("🎨 IMAGE GENERATOR")
        print("="*50)
        
        try:
            description = input("\nDescribe the image you want to create:\n> ").strip()
            
            if not description:
                print("❌ Please provide a description!")
                input("Press Enter to continue...")
                return
            
            print(f"\n⏳ Generating image from: '{description}'...")
            print("\n💡 (In production, this would use Stable Diffusion)")
            
            print("\n✅ Image generation request processed!")
            print(f"   Description: {description}")
            print("   Status: Ready for processing")
            print("   Output: image_output.jpg (would be generated)")
            
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def text_to_speech(self):
        """Convert text to speech"""
        print("\n" + "="*50)
        print("🔊 TEXT TO SPEECH")
        print("="*50)
        
        try:
            text = input("\nEnter text to convert to speech:\n> ").strip()
            
            if not text:
                print("❌ Please provide text!")
                input("Press Enter to continue...")
                return
            
            language = input("Language (en/he/es/fr): ").strip() or 'en'
            
            print(f"\n⏳ Converting '{text}' to speech...")
            
            result = self.ai_engine.text_to_speech(text, language)
            
            if result['success']:
                print(f"\n✅ {result['message']}")
                print(f"   Audio file: {result['file']}")
            else:
                print(f"\n❌ {result['message']}")
            
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def generate_code(self):
        """Generate code in different languages"""
        print("\n" + "="*50)
        print("💻 CODE GENERATOR")
        print("="*50)
        
        print("\nSupported Languages:")
        print("  1. Python")
        print("  2. Java")
        print("  3. JavaScript")
        
        try:
            lang_choice = input("\nChoose language (1-3): ").strip()
            
            languages = {
                '1': 'python',
                '2': 'java',
                '3': 'javascript'
            }
            
            language = languages.get(lang_choice, 'python')
            
            description = input(f"Describe what {language} code you want:\n> ").strip()
            
            if not description:
                description = "A sample script"
            
            print(f"\n⏳ Generating {language.upper()} code...")
            
            result = self.ai_engine.generate_code(language, description)
            
            print("\n✅ Code Generated Successfully!")
            print("\n" + "="*50)
            print(f"CODE ({language.upper()}):")
            print("="*50)
            print(result['code'])
            print("="*50)
            
            # Save to file
            extensions = {'python': 'py', 'java': 'java', 'javascript': 'js'}
            ext = extensions.get(language, 'txt')
            filename = f"generated_code/code_{language}.{ext}"
            
            os.makedirs("generated_code", exist_ok=True)
            
            with open(filename, 'w') as f:
                f.write(result['code'])
            
            print(f"\n💾 Code saved to: {filename}")
            
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
        
        input("\nPress Enter to continue...")
    
    def show_info(self):
        """Show bot information"""
        print("\n" + "="*50)
        print("ℹ️  BOT INFORMATION")
        print("="*50)
        
        info = f"""
Bot Name: {self.bot_name}
Version: {self.version}
Author: Yoav
Status: Online & Ready ✅

Features:
  ✨ Minecraft Mod Generator
  ✨ AI Image Generation
  ✨ Text-to-Speech
  ✨ Code Generation
  ✨ Game Development Helper

Capabilities:
  • Python, Java, JavaScript support
  • Multiple mod types
  • Free and unlimited
  • No API keys required
  • Local processing

System Info:
  • Python Version: {sys.version.split()[0]}
  • Platform: {sys.platform}
  • Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        print(info)
        
        input("Press Enter to continue...")
    
    def show_help(self):
        """Show help and commands"""
        print("\n" + "="*50)
        print("📋 HELP & COMMANDS")
        print("="*50)
        
        help_text = """
MAIN COMMANDS:
  1. Create Minecraft Mod
     - Choose mod type (basic, tool, block, entity)
     - Name your mod
     - Get generated code instantly

  2. Generate Image
     - Describe what image you want
     - Get AI image generation
     - Save and use the image

  3. Text to Speech
     - Enter any text
     - Choose language
     - Convert to audio file

  4. Generate Code
     - Choose programming language
     - Describe what you need
     - Get ready-to-use code

TIPS & TRICKS:
  • All generated files are saved locally
  • You can edit and customize any output
  • No internet required for most features
  • All processing is free!
  • Use 'Exit' to quit anytime

KEYBOARD SHORTCUTS:
  • Ctrl+C to stop any operation
  • Type 'exit' or '7' to quit
  • Press Enter to continue after each action

TROUBLESHOOTING:
  • If text-to-speech fails, check gTTS installation
  • Make sure Python 3.9+ is installed
  • Check folder permissions for saving files
  • Run 'pip install -r requirements.txt' if needed

FOR MORE HELP:
  • Check README.md
  • Visit GitHub: yoavsorias-collab/yoavbot
  • Create an issue with your problem
        """
        print(help_text)
        
        input("Press Enter to continue...")
    
    def run(self):
        """Main loop"""
        self.clear_screen()
        self.print_banner()
        
        print("\n✅ Yoav Bot started successfully!")
        print("⏳ Loading modules...\n")
        
        try:
            while self.running:
                self.print_menu()
                
                choice = input("Enter your choice (1-7): ").strip()
                
                if choice == '1':
                    self.create_minecraft_mod()
                elif choice == '2':
                    self.generate_image()
                elif choice == '3':
                    self.text_to_speech()
                elif choice == '4':
                    self.generate_code()
                elif choice == '5':
                    self.show_info()
                elif choice == '6':
                    self.show_help()
                elif choice == '7' or choice.lower() == 'exit':
                    self.exit_bot()
                else:
                    print("\n❌ Invalid choice! Please enter 1-7.")
                    input("Press Enter to continue...")
        
        except KeyboardInterrupt:
            print("\n\n⏹️  Bot interrupted by user.")
            self.exit_bot()
        except Exception as e:
            print(f"\n❌ Unexpected error: {str(e)}")
            self.exit_bot()
    
    def exit_bot(self):
        """Exit the bot gracefully"""
        self.running = False
        
        print("\n" + "="*50)
        print("👋 Thank you for using Yoav Bot!")
        print("="*50)
        print("\n✨ Goodbye! See you next time!")
        print("📚 For more features, check out:")
        print("   • Discord Bot")
        print("   • Web Interface")
        print("   • Telegram Bot")
        print("\n🚀 Happy coding!\n")
        
        sys.exit(0)

def main():
    """Entry point"""
    try:
        bot = YoavBotCLI()
        bot.run()
    except Exception as e:
        print(f"\n❌ Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
