import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import os

def create_package_image(output_path, radius=3, rows=2, cols=4):
    """Generate an image of packed spheres in a rectangle"""
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        diameter = 2 * radius
        width = cols * diameter
        height = rows * diameter
        
        fig, ax = plt.subplots(figsize=(8, 4))
        
        # Draw rectangle
        ax.add_patch(Rectangle((0, 0), width, height, fill=False, linewidth=2))
        
        # Draw circles
        for row in range(rows):
            for col in range(cols):
                x = radius + col * diameter
                y = radius + row * diameter
                ax.add_patch(Circle((x, y), radius, fill=False, linewidth=1.5))
        
        ax.set_xlim(0, width)
        ax.set_ylim(0, height)
        ax.set_aspect('equal')
        plt.axis('off')
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Image successfully saved to: {output_path}")
    except Exception as e:
        print(f"Error generating image: {e}")