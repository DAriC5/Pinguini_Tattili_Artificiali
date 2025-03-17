import gymnasium as gym
import numpy as np
from gymnasium import spaces
from gymnasium.envs.registration import register

class GridWorldEnv(gym.Env):
    def __init__(self, render_mode=None, grid_size = 5):
        super().__init__()

        # Salva il render_mode
        self.render_mode = render_mode
        
        # Dimensioni della griglia
        self.grid_size = grid_size

        self.grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
        
        # Definiamo lo spazio delle azioni: 0=su, 1=destra, 2=giù, 3=sinistra
        self.action_space = spaces.Discrete(8)
        
        # Definiamo lo spazio delle osservazioni: posizione [x, y] sulla griglia
        self.observation_space = spaces.Box(
            low=0, high=self.grid_size-1, 
            shape=(2,), dtype=np.int32
        )
        
        # Posizione iniziale e posizione obiettivo
        self.agent_pos = None
        self.target_pos = [self.grid_size-1, self.grid_size-1]  # Angolo in basso a destra
        
        # Resetta l'ambiente
        self.reset()
        
    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        
        # Posiziona l'agente in alto a sinistra
        self.agent_pos = [0, 0]
        
        # Restituisci l'osservazione iniziale e info aggiuntive
        observation = np.array(self.agent_pos)
        info = {}
        
        return observation, info
    
    def step(self, action):
        # Copia la posizione attuale
        new_pos = self.agent_pos.copy()
        
        # Modifica la posizione in base all'azione
        if action == 0:  # Su
            new_pos[1] = max(0, new_pos[1] - 1)
        elif action == 1:  # Destra
            new_pos[0] = min(self.grid_size - 1, new_pos[0] + 1)
        elif action == 2:  # Giù
            new_pos[1] = min(self.grid_size - 1, new_pos[1] + 1)
        elif action == 3:  # Sinistra
            new_pos[0] = max(0, new_pos[0] - 1)
        elif action == 4: #alto destra
            new_pos[1] = max(0, new_pos[1] - 1)  
            new_pos[0] = min(self.grid_size - 1, new_pos[0] + 1)
        elif action == 5: #alto sinistra
            new_pos[1] = max(0, new_pos[1] - 1)
            new_pos[0] = max(0, new_pos[0] - 1)
        elif action == 6: #basso destra
            new_pos[1] = min(self.grid_size - 1, new_pos[1] + 1)
            new_pos[0] = min(self.grid_size - 1, new_pos[0] + 1)
        elif action == 7: #basso sinistra
            new_pos[1] = min(self.grid_size - 1, new_pos[1] + 1)
            new_pos[0] = max(0, new_pos[0] - 1)

        # Aggiorna la posizione dell'agente
        self.agent_pos = new_pos
        
        # lascia la ricompensa a 0 se non ha trovat il premio
        reward = 0
        
        # Controlla se l'episodio è terminato (agente ha raggiunto l'obiettivo)
        terminated = np.array_equal(self.agent_pos, self.target_pos)
        if terminated:
            reward = 10

        if self.grid[self.agent_pos[0]][self.agent_pos[1]] == " ":
            reward = -10
            terminated = True
        
        # Prepara l'output
        observation = np.array(self.agent_pos)
        truncated = False  # True se l'episodio termina per altri motivi (es. limite di passi)
        info = {}
        
        return observation, reward, terminated, truncated, info
    
    def render(self):        
        # Posiziona l'agente e l'obiettivo
        self.grid[self.agent_pos[1]][self.agent_pos[0]] = 'A'
        self.grid[self.target_pos[1]][self.target_pos[0]] = 'T'
        
        # Stampa la griglia
        for row in self.grid:
            print(' '.join(row))
        print()

        self.grid[self.agent_pos[1]][self.agent_pos[0]] = ' '
        self.grid[self.target_pos[1]][self.target_pos[0]] = ' '

# Registra l'ambiente
register(
    id='GridWorld-v0',
    entry_point='evirorment:GridWorldEnv',
    max_episode_steps=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
)

# Esempio di utilizzo
if __name__ == "__main__":
    import gymnasium as gym
    
    # Crea l'ambiente
    env = gym.make('GridWorld-v0')  

    # Resetta l'ambiente
    observation, info = env.reset()
    print("Stato iniziale:", observation)
    
    # Ciclo di gioco
    total_reward = 0
    passi = 0
    while (True):
        passi += 1

        # Scegli un'azione casuale
        action = env.action_space.sample() 
        
        pos_precedente = observation.copy()
        # Esegui l'azione
        observation, reward, terminated, truncated, info = env.step(action)
        total_reward = reward
        
        # Stampa i risultati
        print(f"Passo {passi}: Azione: {action}, Posizione: {observation}, Ricompensa: {reward}")
        env.unwrapped.render() #unwrapped fa accedere alla mia funzione e non a quela di gym

        # Termina se l'episodio è finito
        if terminated or truncated:
            print(f"Episodio terminato! Ricompensa totale: {total_reward}")
            break
    
    env.close()