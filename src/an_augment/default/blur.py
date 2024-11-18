from scipy.ndimage import gaussian_filter, uniform_filter, median_filter
import numpy as np
import cv2

def motion_blur(image, length=5, angle=0):
    """
    Applies motion blur to an image.

    Parameters:
    - image (np.array): Input image as a 2D or 3D numpy array.
    - length (int): Length of the motion blur effect.
    - angle (float): Angle of motion blur in degrees.

    Returns:
    - np.array: Motion-blurred image.
    """
    kernel = np.zeros((length, length))
    center = length // 2
    radians = np.deg2rad(angle)
    x = int(center + np.cos(radians) * center)
    y = int(center + np.sin(radians) * center)
    
    kernel[center, :] = 1
    kernel /= kernel.sum()
    return cv2.filter2D(image, -1, kernel)

def blur(image, blur_type='gaussian', blur_radius=1, **kwargs):
    """
    Applies blur to a given image.

    Parameters:
    - image (np.array): Input image as a 2D or 3D numpy array.
    - blur_type (str): Type of blur to apply ('gaussian', 'uniform', 'median', 'motion').
    - blur_radius (float): Standard deviation for Gaussian kernel or size for uniform/median filter. Higher values increase blur.
    - **kwargs: Additional parameters for specific blur types (e.g., length, angle for motion blur).

    Returns:
    - np.array: Blurred image with the same shape as input.
    """
    if blur_type == 'gaussian':
        return gaussian_filter(image, sigma=blur_radius)
    elif blur_type == 'uniform':
        return uniform_filter(image, size=int(blur_radius))
    elif blur_type == 'median':
        return median_filter(image, size=int(blur_radius))
    elif blur_type == 'motion':
        length = kwargs.get('length', 5)
        angle = kwargs.get('angle', 0)
        return motion_blur(image, length=length, angle=angle)
    else:
        raise ValueError("Unsupported blur type. Use 'gaussian', 'uniform', 'median', or 'motion'.")
