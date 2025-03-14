import json
import os

class LockerManager:
    def __init__(self, locker_file='locker.json'):
        self.locker_file = locker_file
        self.locker_data = self.load_locker()

    def load_locker(self):
        """Load the locker.json file."""
        if os.path.exists(self.locker_file):
            with open(self.locker_file, 'r') as file:
                return json.load(file)
        return {"servers": {}}

    def save_locker(self):
        """Save the locker data to locker.json."""
        with open(self.locker_file, 'w') as file:
            json.dump(self.locker_data, file, indent=4)

    def initialize_locker(self):
        """Initialize locker.json with an empty structure."""
        print(f"Creating a new locker file at {self.locker_file}...")
        self.locker_data = {"servers": {}}
        self.save_locker()

    def add_server(self, server_type):
        """Add a new server type."""
        if server_type in self.locker_data["servers"]:
            print(f"Server type {server_type} already exists.")
        else:
            self.locker_data["servers"][server_type] = []
            print(f"Server type {server_type} added.")
            self.save_locker()

    def add_version(self, server_type, version, url, supports_plugins):
        """Add a new version to a server type."""
        if server_type not in self.locker_data["servers"]:
            print(f"Server type {server_type} does not exist. Please add it first.")
            return

        versions = self.locker_data["servers"][server_type]
        if any(v['version'] == version for v in versions):
            print(f"Version {version} already exists for {server_type}.")
        else:
            new_version = {
                "version": version,
                "url": url,
                "supports_plugins": supports_plugins
            }
            versions.append(new_version)
            print(f"Version {version} added to {server_type}.")
            self.save_locker()

    def update_version(self, server_type, version, url):
        """Update the URL for an existing version."""
        if server_type not in self.locker_data["servers"]:
            print(f"Server type {server_type} does not exist.")
            return

        versions = self.locker_data["servers"][server_type]
        for v in versions:
            if v['version'] == version:
                v['url'] = url
                print(f"Version {version} URL updated for {server_type}.")
                self.save_locker()
                return
        print(f"Version {version} not found for {server_type}.")

    def remove_version(self, server_type, version):
        """Remove a version from a server type."""
        if server_type not in self.locker_data["servers"]:
            print(f"Server type {server_type} does not exist.")
            return

        versions = self.locker_data["servers"][server_type]
        versions = [v for v in versions if v['version'] != version]
        self.locker_data["servers"][server_type] = versions
        print(f"Version {version} removed from {server_type}.")
        self.save_locker()