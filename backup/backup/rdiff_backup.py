import subprocess


class RdiffBackup:

    def backup_simple(self, source: str, destination: str):
        self.backup(
            source,
            destination,
        )

    def backup_include(self, source: str, destination: str, include_list, verbosity_level="-v5"):
        self.backup(
            source,
            destination,
            verbosity_level,
            include_list,
            None
        )

    def backup_exclude(self, source: str, destination: str, exclude_list, verbosity_level="-v5"):
        self.backup(
            source,
            destination,
            verbosity_level,
            None,
            exclude_list
        )

    def backup(self, source: str, destination: str, verbosity_level="-v5", include_list=None, exclude_list=None):
        args = [
            "rdiff-backup",
            verbosity_level
        ]

        if include_list is not None:
            args.append("--include-filelist")
            args.append(include_list)

        if exclude_list is not None:
            args.append("--exclude-filelist")
            args.append(exclude_list)

        args.append(source)
        args.append(destination)

        command = subprocess.run(
            args,
            capture_output=True)

        return command.stderr, command.stdout
