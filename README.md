Here's a well-structured **README.md** file for your GitHub repository:  

---

# **🐍 Snake, Water, Gun Game 🎮**  

A fun **Snake, Water, and Gun** game that I played in school! This is a simple Python-based command-line game where you play against the system, which randomly selects its choice.  

## **🚀 Features**  
✅ Uses Python's `random.choice()` function to make the game fair.  
✅ Implements a dictionary-based approach for user-friendly inputs.  
✅ A simple **if-else ladder** determines the game outcome.  
✅ Provides clear and engaging win/loss messages.  

## **📜 Rules**  
- **Snake (S) 🐍 beats Water (W) 💦** → *Snake drinks all the water*  
- **Water (W) 💦 beats Gun (G) 🔫** → *Guns don't work in water*  
- **Gun (G) 🔫 beats Snake (S) 🐍** → *Gun kills the snake*  
- If both the **player** and **system** choose the same option, it's a **draw!**  

## **🛠 How to Play**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/snake-water-gun-game.git
   ```
2. Navigate to the project directory:  
   ```bash
   cd snake-water-gun-game
   ```
3. Run the Python script:  
   ```bash
   python game.py
   ```
4. Enter your choice when prompted:  
   ```
   Enter your choice (s for Snake, w for Water, g for Gun): 
   ```
5. The system will generate its choice randomly, and the winner will be announced! 🎉  

## **📝 Code Overview**  
- Uses **random module** to generate system choices.  
- Implements a **dictionary mapping** for easy input handling.  
- Simple **if-else logic** to determine the winner.  

## **📌 Example Output**  
```
Enter your choice (s for Snake, w for Water, g for Gun): s
You chose Snake 🐍  
The system chose Gun 🔫  
Oops! System Won! Snake killed by a gunshot!  
```

## **📌 Contributing**  
Feel free to fork this repository, improve the code, and submit a pull request!
