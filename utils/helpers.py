import os
import time
from datetime import datetime


class Helpers:
    """Common helper functions"""

    @staticmethod
    def create_directory(path):
        """Create a directory if it doesn't exist"""
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def get_timestamp():
        """Get current timestamp"""
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    @staticmethod
    def wait(seconds):
        """Wait for specified seconds"""
        time.sleep(seconds)

    @staticmethod
    def generate_unique_filename(prefix="", extension=""):
        """Generate unique filename with timestamp"""
        timestamp = Helpers.get_timestamp()
        filename = f"{prefix}_{timestamp}{extension}" if prefix else f"{timestamp}{extension}"
        return filename

    @staticmethod
    def ensure_screenshot_dir():
        """Ensure a screenshot directory exists"""
        screenshot_dir = "test-results/screenshots"
        Helpers.create_directory(screenshot_dir)
        return screenshot_dir

    @staticmethod
    def ensure_video_dir():
        """Ensure video directory exists"""
        video_dir = "test-results/videos"
        Helpers.create_directory(video_dir)
        return video_dir

    @staticmethod
    def ensure_trace_dir():
        """Ensure a trace directory exists"""
        trace_dir = "test-results/traces"
        Helpers.create_directory(trace_dir)
        return trace_dir
