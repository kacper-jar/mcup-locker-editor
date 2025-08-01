import argparse
from locker_manager import LockerManager


class LockerTool:
    def __init__(self):
        self.manager = LockerManager()

    def init_locker(self):
        """Initialize locker.json file."""
        print("Initializing locker.json...")
        self.manager.initialize_locker()

    def add_server(self, server_type):
        """Add a new server type (e.g., vanilla, spigot)."""
        print(f"Adding new server type: {server_type}...")
        self.manager.add_server(server_type)

    def add_version(self, server_type, version, source, url_target, supports_plugins, supports_mods, third_party_warning, configs):
        """Add a new version for a server type."""
        print(f"Adding version {version} for {server_type}...")
        self.manager.add_version(server_type, version, source, url_target, supports_plugins, supports_mods, third_party_warning, configs)

    def update_version(self, server_type, version, url):
        """Update the URL for an existing version."""
        print(f"Updating version {version} for {server_type}...")
        self.manager.update_version(server_type, version, url)

    def remove_version(self, server_type, version):
        """Remove a version from a server type."""
        print(f"Removing version {version} for {server_type}...")
        self.manager.remove_version(server_type, version)

    def run(self):
        """Parse arguments and run the appropriate function."""
        parser = argparse.ArgumentParser(description="Manage mcup locker file (locker.json)")

        subparsers = parser.add_subparsers()

        init_locker_parser = subparsers.add_parser('init', help="Initialize locker.json")
        init_locker_parser.set_defaults(func=lambda args: self.init_locker())

        add_server_parser = subparsers.add_parser('add-server', help="Add a new server type (e.g., vanilla, spigot)")
        add_server_parser.add_argument('server_type', help="Server type (e.g., vanilla, spigot)")
        add_server_parser.set_defaults(func=lambda args: self.add_server(args.server_type))

        add_downloadable_version_parser = subparsers.add_parser('add-downloadable-version', help="Add a downloadable version for a server type")
        add_downloadable_version_parser.add_argument('server_type', help="Server type (e.g., vanilla, spigot)")
        add_downloadable_version_parser.add_argument('version', help="Version (e.g., 1.20.4)")
        add_downloadable_version_parser.add_argument('url', help="Download URL for the server version")
        add_downloadable_version_parser.add_argument('supports_plugins',
                                        help="Whether the version supports plugins (True/False)")
        add_downloadable_version_parser.add_argument('supports_mods',
                                                     help="Whether the version supports mods (True/False)")
        add_downloadable_version_parser.add_argument('third_party_warning',
                                                     help="Whether the version has a third party warning displayed before download (True/False)")
        add_downloadable_version_parser.add_argument('configs', nargs='*',
                                                     help="List of configuration files required for the server version")
        add_downloadable_version_parser.set_defaults(
            func=lambda args: self.add_version(args.server_type, args.version, "DOWNLOAD", args.url,
                                               args.supports_plugins, args.supports_mods,
                                               args.third_party_warning, args.configs))

        add_buildtools_version_parser = subparsers.add_parser('add-buildtools-version', help="Add a version requiring BuildTools to get for a server type")
        add_buildtools_version_parser.add_argument('server_type', help="Server type (e.g., vanilla, spigot)")
        add_buildtools_version_parser.add_argument('version', help="Version (e.g., 1.20.4)")
        add_buildtools_version_parser.add_argument('target', help="Target name for the BuildTools to build")
        add_buildtools_version_parser.add_argument('supports_plugins',
                                                   help="Whether the version supports plugins (True/False)")
        add_buildtools_version_parser.add_argument('supports_mods',
                                                   help="Whether the version supports mods (True/False)")
        add_buildtools_version_parser.add_argument('third_party_warning',
                                                   help="Whether the version has a third party warning displayed before download (True/False)")
        add_buildtools_version_parser.add_argument('configs', nargs='*',
                                                   help="List of configuration files required for the server version")
        add_buildtools_version_parser.set_defaults(
            func=lambda args: self.add_version(args.server_type, args.version, "BUILDTOOLS", args.target,
                                               args.supports_plugins, args.supports_mods,
                                               args.third_party_warning, args.configs))

        update_version_parser = subparsers.add_parser('update-version', help="Update the URL for an existing version")
        update_version_parser.add_argument('server_type', help="Server type (e.g., vanilla, spigot)")
        update_version_parser.add_argument('version', help="Version (e.g., 1.20.4)")
        update_version_parser.add_argument('url', help="New download URL for the server version")
        update_version_parser.set_defaults(
            func=lambda args: self.update_version(args.server_type, args.version, args.url))

        remove_version_parser = subparsers.add_parser('remove-version', help="Remove a version for a server type")
        remove_version_parser.add_argument('server_type', help="Server type (e.g., vanilla, spigot)")
        remove_version_parser.add_argument('version', help="Version to be removed (e.g., 1.19.2)")
        remove_version_parser.set_defaults(func=lambda args: self.remove_version(args.server_type, args.version))

        list_parser = subparsers.add_parser('list', help="Display a list of current locker file configuration")
        list_parser.set_defaults(func=lambda args: self.manager.list_locker())

        args = parser.parse_args()
        if hasattr(args, "func"):
            args.func(args)
        else:
            parser.print_help()


if __name__ == '__main__':
    tool = LockerTool()
    tool.run()
