import alchemy
from alchemy.transmutation import lead_to_gold, stone_to_gem
from alchemy.transmutation import philosophers_stone, elixir_of_life


if __name__ == "__main__":
    print()
    print("=== Pathway Debate Mastery ===")
    print()
    print("Testing absolute Imports (from basic.py):")
    print("lead_to_gold():", lead_to_gold())
    print("stone_to_gem():", stone_to_gem())
    print()
    print("Testing Realtive Imports (from advanced.py):")
    print("philosophers_stone():", philosophers_stone())
    print("elixir_of_life():", elixir_of_life())
    print()
    print("Testing Package Access:")
    print("alchemy.transmutation.lead_to_gold():",
          alchemy.transmutation.lead_to_gold())
    print("alchemy.transmutation.philosophers_stone()",
          alchemy.transmutation.philosophers_stone())
    print()
    print("Both pathways work! Absolute: clear, Realtive: concise")
