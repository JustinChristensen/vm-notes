```
[wroathe@rohan:~] $ ps 699
  PID TTY      STAT   TIME COMMAND
  699 ?        S      0:00 sshd: wroathe@pts/0
[wroathe@rohan:~] $ sudo cat /proc/699/maps
563db394d000-563db3a0a000 r-xp 00000000 08:01 1321888                    /usr/sbin/sshd
563db3c09000-563db3c0c000 r--p 000bc000 08:01 1321888                    /usr/sbin/sshd
563db3c0c000-563db3c0d000 rw-p 000bf000 08:01 1321888                    /usr/sbin/sshd
563db3c0d000-563db3c16000 rw-p 00000000 00:00 0
563db3ec4000-563db3ef4000 rw-p 00000000 00:00 0                          [heap]
7f45afe43000-7f45afe7e000 r-xp 00000000 08:01 1179785                    /lib/x86_64-linux-gnu/libnss_systemd.so.2
7f45afe7e000-7f45b007d000 ---p 0003b000 08:01 1179785                    /lib/x86_64-linux-gnu/libnss_systemd.so.2
7f45b007d000-7f45b0080000 r--p 0003a000 08:01 1179785                    /lib/x86_64-linux-gnu/libnss_systemd.so.2
7f45b0080000-7f45b0081000 rw-p 0003d000 08:01 1179785                    /lib/x86_64-linux-gnu/libnss_systemd.so.2
7f45b0081000-7f45b0084000 r-xp 00000000 08:01 1179740                    /lib/x86_64-linux-gnu/security/pam_env.so
7f45b0084000-7f45b0283000 ---p 00003000 08:01 1179740                    /lib/x86_64-linux-gnu/security/pam_env.so
7f45b0283000-7f45b0284000 r--p 00002000 08:01 1179740                    /lib/x86_64-linux-gnu/security/pam_env.so
7f45b0284000-7f45b0285000 rw-p 00003000 08:01 1179740                    /lib/x86_64-linux-gnu/security/pam_env.so
7f45b0285000-7f45b028a000 r-xp 00000000 08:01 1179778                    /lib/x86_64-linux-gnu/security/pam_limits.so
7f45b028a000-7f45b0489000 ---p 00005000 08:01 1179778                    /lib/x86_64-linux-gnu/security/pam_limits.so
7f45b0489000-7f45b048a000 r--p 00004000 08:01 1179778                    /lib/x86_64-linux-gnu/security/pam_limits.so
7f45b048a000-7f45b048b000 rw-p 00005000 08:01 1179778                    /lib/x86_64-linux-gnu/security/pam_limits.so
7f45b048b000-7f45b048d000 r-xp 00000000 08:01 1179782                    /lib/x86_64-linux-gnu/security/pam_mail.so
7f45b048d000-7f45b068c000 ---p 00002000 08:01 1179782                    /lib/x86_64-linux-gnu/security/pam_mail.so
7f45b068c000-7f45b068d000 r--p 00001000 08:01 1179782                    /lib/x86_64-linux-gnu/security/pam_mail.so
7f45b068d000-7f45b068e000 rw-p 00002000 08:01 1179782                    /lib/x86_64-linux-gnu/security/pam_mail.so
7f45b068e000-7f45b0690000 r-xp 00000000 08:01 1179784                    /lib/x86_64-linux-gnu/security/pam_motd.so
7f45b0690000-7f45b088f000 ---p 00002000 08:01 1179784                    /lib/x86_64-linux-gnu/security/pam_motd.so
7f45b088f000-7f45b0890000 r--p 00001000 08:01 1179784                    /lib/x86_64-linux-gnu/security/pam_motd.so
7f45b0890000-7f45b0891000 rw-p 00002000 08:01 1179784                    /lib/x86_64-linux-gnu/security/pam_motd.so
7f45b0891000-7f45b0894000 r-xp 00000000 08:01 1179764                    /lib/x86_64-linux-gnu/libpam_misc.so.0.82.0
7f45b0894000-7f45b0a93000 ---p 00003000 08:01 1179764                    /lib/x86_64-linux-gnu/libpam_misc.so.0.82.0
7f45b0a93000-7f45b0a94000 r--p 00002000 08:01 1179764                    /lib/x86_64-linux-gnu/libpam_misc.so.0.82.0
7f45b0a94000-7f45b0a95000 rw-p 00003000 08:01 1179764                    /lib/x86_64-linux-gnu/libpam_misc.so.0.82.0
7f45b0a95000-7f45b0ad1000 r-xp 00000000 08:01 1179652                    /lib/x86_64-linux-gnu/security/pam_systemd.so
7f45b0ad1000-7f45b0cd0000 ---p 0003c000 08:01 1179652                    /lib/x86_64-linux-gnu/security/pam_systemd.so
7f45b0cd0000-7f45b0cd3000 r--p 0003b000 08:01 1179652                    /lib/x86_64-linux-gnu/security/pam_systemd.so
7f45b0cd3000-7f45b0cd4000 rw-p 0003e000 08:01 1179652                    /lib/x86_64-linux-gnu/security/pam_systemd.so
7f45b0cd4000-7f45b0cd6000 r-xp 00000000 08:01 1179920                    /lib/x86_64-linux-gnu/security/pam_umask.so
7f45b0cd6000-7f45b0ed5000 ---p 00002000 08:01 1179920                    /lib/x86_64-linux-gnu/security/pam_umask.so
7f45b0ed5000-7f45b0ed6000 r--p 00001000 08:01 1179920                    /lib/x86_64-linux-gnu/security/pam_umask.so
7f45b0ed6000-7f45b0ed7000 rw-p 00002000 08:01 1179920                    /lib/x86_64-linux-gnu/security/pam_umask.so
7f45b0ed7000-7f45b0ed9000 r-xp 00000000 08:01 1179776                    /lib/x86_64-linux-gnu/security/pam_keyinit.so
7f45b0ed9000-7f45b10d8000 ---p 00002000 08:01 1179776                    /lib/x86_64-linux-gnu/security/pam_keyinit.so
7f45b10d8000-7f45b10d9000 r--p 00001000 08:01 1179776                    /lib/x86_64-linux-gnu/security/pam_keyinit.so
7f45b10d9000-7f45b10da000 rw-p 00002000 08:01 1179776                    /lib/x86_64-linux-gnu/security/pam_keyinit.so
7f45b10da000-7f45b10dc000 r-xp 00000000 08:01 1179781                    /lib/x86_64-linux-gnu/security/pam_loginuid.so
7f45b10dc000-7f45b12db000 ---p 00002000 08:01 1179781                    /lib/x86_64-linux-gnu/security/pam_loginuid.so
7f45b12db000-7f45b12dc000 r--p 00001000 08:01 1179781                    /lib/x86_64-linux-gnu/security/pam_loginuid.so
7f45b12dc000-7f45b12dd000 rw-p 00002000 08:01 1179781                    /lib/x86_64-linux-gnu/security/pam_loginuid.so
7f45b12dd000-7f45b12e1000 r-xp 00000000 08:01 1179794                    /lib/x86_64-linux-gnu/security/pam_selinux.so
7f45b12e1000-7f45b14e0000 ---p 00004000 08:01 1179794                    /lib/x86_64-linux-gnu/security/pam_selinux.so
7f45b14e0000-7f45b14e1000 r--p 00003000 08:01 1179794                    /lib/x86_64-linux-gnu/security/pam_selinux.so
7f45b14e1000-7f45b14e2000 rw-p 00004000 08:01 1179794                    /lib/x86_64-linux-gnu/security/pam_selinux.so
7f45b14e2000-7f45b14e3000 r-xp 00000000 08:01 1179787                    /lib/x86_64-linux-gnu/security/pam_nologin.so
7f45b14e3000-7f45b16e3000 ---p 00001000 08:01 1179787                    /lib/x86_64-linux-gnu/security/pam_nologin.so
7f45b16e3000-7f45b16e4000 r--p 00001000 08:01 1179787                    /lib/x86_64-linux-gnu/security/pam_nologin.so
7f45b16e4000-7f45b16e5000 rw-p 00002000 08:01 1179787                    /lib/x86_64-linux-gnu/security/pam_nologin.so
7f45b16e5000-7f45b16e9000 r-xp 00000000 08:01 1179820                    /lib/x86_64-linux-gnu/libcap.so.2.25
7f45b16e9000-7f45b18e9000 ---p 00004000 08:01 1179820                    /lib/x86_64-linux-gnu/libcap.so.2.25
7f45b18e9000-7f45b18ea000 r--p 00004000 08:01 1179820                    /lib/x86_64-linux-gnu/libcap.so.2.25
7f45b18ea000-7f45b18eb000 rw-p 00005000 08:01 1179820                    /lib/x86_64-linux-gnu/libcap.so.2.25
7f45b18eb000-7f45b18ed000 r-xp 00000000 08:01 1180226                    /lib/x86_64-linux-gnu/security/pam_cap.so
7f45b18ed000-7f45b1aec000 ---p 00002000 08:01 1180226                    /lib/x86_64-linux-gnu/security/pam_cap.so
7f45b1aec000-7f45b1aed000 r--p 00001000 08:01 1180226                    /lib/x86_64-linux-gnu/security/pam_cap.so
7f45b1aed000-7f45b1aee000 rw-p 00002000 08:01 1180226                    /lib/x86_64-linux-gnu/security/pam_cap.so
7f45b1aee000-7f45b1aef000 r-xp 00000000 08:01 1179788                    /lib/x86_64-linux-gnu/security/pam_permit.so
7f45b1aef000-7f45b1cee000 ---p 00001000 08:01 1179788                    /lib/x86_64-linux-gnu/security/pam_permit.so
7f45b1cee000-7f45b1cef000 r--p 00000000 08:01 1179788                    /lib/x86_64-linux-gnu/security/pam_permit.so
7f45b1cef000-7f45b1cf0000 rw-p 00001000 08:01 1179788                    /lib/x86_64-linux-gnu/security/pam_permit.so
7f45b1cf0000-7f45b1cf1000 r-xp 00000000 08:01 1179737                    /lib/x86_64-linux-gnu/security/pam_deny.so
7f45b1cf1000-7f45b1ef0000 ---p 00001000 08:01 1179737                    /lib/x86_64-linux-gnu/security/pam_deny.so
7f45b1ef0000-7f45b1ef1000 r--p 00000000 08:01 1179737                    /lib/x86_64-linux-gnu/security/pam_deny.so
7f45b1ef1000-7f45b1ef2000 rw-p 00001000 08:01 1179737                    /lib/x86_64-linux-gnu/security/pam_deny.so
7f45b1ef2000-7f45b1eff000 r-xp 00000000 08:01 1180288                    /lib/x86_64-linux-gnu/security/pam_unix.so
7f45b1eff000-7f45b20ff000 ---p 0000d000 08:01 1180288                    /lib/x86_64-linux-gnu/security/pam_unix.so
7f45b20ff000-7f45b2100000 r--p 0000d000 08:01 1180288                    /lib/x86_64-linux-gnu/security/pam_unix.so
7f45b2100000-7f45b2101000 rw-p 0000e000 08:01 1180288                    /lib/x86_64-linux-gnu/security/pam_unix.so
7f45b2101000-7f45b210d000 rw-p 00000000 00:00 0
7f45b210d000-7f45b2118000 r-xp 00000000 08:01 1179682                    /lib/x86_64-linux-gnu/libnss_files-2.27.so
7f45b2118000-7f45b2317000 ---p 0000b000 08:01 1179682                    /lib/x86_64-linux-gnu/libnss_files-2.27.so
7f45b2317000-7f45b2318000 r--p 0000a000 08:01 1179682                    /lib/x86_64-linux-gnu/libnss_files-2.27.so
7f45b2318000-7f45b2319000 rw-p 0000b000 08:01 1179682                    /lib/x86_64-linux-gnu/libnss_files-2.27.so
7f45b2319000-7f45b231f000 rw-p 00000000 00:00 0
7f45b231f000-7f45b232a000 r-xp 00000000 08:01 1179684                    /lib/x86_64-linux-gnu/libnss_nis-2.27.so
7f45b232a000-7f45b2529000 ---p 0000b000 08:01 1179684                    /lib/x86_64-linux-gnu/libnss_nis-2.27.so
7f45b2529000-7f45b252a000 r--p 0000a000 08:01 1179684                    /lib/x86_64-linux-gnu/libnss_nis-2.27.so
7f45b252a000-7f45b252b000 rw-p 0000b000 08:01 1179684                    /lib/x86_64-linux-gnu/libnss_nis-2.27.so
7f45b252b000-7f45b2533000 r-xp 00000000 08:01 1179680                    /lib/x86_64-linux-gnu/libnss_compat-2.27.so
7f45b2533000-7f45b2733000 ---p 00008000 08:01 1179680                    /lib/x86_64-linux-gnu/libnss_compat-2.27.so
7f45b2733000-7f45b2734000 r--p 00008000 08:01 1179680                    /lib/x86_64-linux-gnu/libnss_compat-2.27.so
7f45b2734000-7f45b2735000 rw-p 00009000 08:01 1179680                    /lib/x86_64-linux-gnu/libnss_compat-2.27.so
7f45b2735000-7f45b2749000 r-xp 00000000 08:01 1179714                    /lib/x86_64-linux-gnu/libgpg-error.so.0.22.0
7f45b2749000-7f45b2948000 ---p 00014000 08:01 1179714                    /lib/x86_64-linux-gnu/libgpg-error.so.0.22.0
7f45b2948000-7f45b2949000 r--p 00013000 08:01 1179714                    /lib/x86_64-linux-gnu/libgpg-error.so.0.22.0
7f45b2949000-7f45b294a000 rw-p 00014000 08:01 1179714                    /lib/x86_64-linux-gnu/libgpg-error.so.0.22.0
7f45b294a000-7f45b2961000 r-xp 00000000 08:01 1179688                    /lib/x86_64-linux-gnu/libresolv-2.27.so
7f45b2961000-7f45b2b61000 ---p 00017000 08:01 1179688                    /lib/x86_64-linux-gnu/libresolv-2.27.so
7f45b2b61000-7f45b2b62000 r--p 00017000 08:01 1179688                    /lib/x86_64-linux-gnu/libresolv-2.27.so
7f45b2b62000-7f45b2b63000 rw-p 00018000 08:01 1179688                    /lib/x86_64-linux-gnu/libresolv-2.27.so
7f45b2b63000-7f45b2b65000 rw-p 00000000 00:00 0
7f45b2b65000-7f45b2b68000 r-xp 00000000 08:01 1179925                    /lib/x86_64-linux-gnu/libkeyutils.so.1.5
7f45b2b68000-7f45b2d67000 ---p 00003000 08:01 1179925                    /lib/x86_64-linux-gnu/libkeyutils.so.1.5
7f45b2d67000-7f45b2d68000 r--p 00002000 08:01 1179925                    /lib/x86_64-linux-gnu/libkeyutils.so.1.5
7f45b2d68000-7f45b2d69000 rw-p 00003000 08:01 1179925                    /lib/x86_64-linux-gnu/libkeyutils.so.1.5
7f45b2d69000-7f45b2d73000 r-xp 00000000 08:01 1321201                    /usr/lib/x86_64-linux-gnu/libkrb5support.so.0.1
7f45b2d73000-7f45b2f72000 ---p 0000a000 08:01 1321201                    /usr/lib/x86_64-linux-gnu/libkrb5support.so.0.1
7f45b2f72000-7f45b2f73000 r--p 00009000 08:01 1321201                    /usr/lib/x86_64-linux-gnu/libkrb5support.so.0.1
7f45b2f73000-7f45b2f74000 rw-p 0000a000 08:01 1321201                    /usr/lib/x86_64-linux-gnu/libkrb5support.so.0.1
7f45b2f74000-7f45b2fa2000 r-xp 00000000 08:01 1321203                    /usr/lib/x86_64-linux-gnu/libk5crypto.so.3.1
7f45b2fa2000-7f45b31a2000 ---p 0002e000 08:01 1321203                    /usr/lib/x86_64-linux-gnu/libk5crypto.so.3.1
7f45b31a2000-7f45b31a4000 r--p 0002e000 08:01 1321203                    /usr/lib/x86_64-linux-gnu/libk5crypto.so.3.1
7f45b31a4000-7f45b31a5000 rw-p 00030000 08:01 1321203                    /usr/lib/x86_64-linux-gnu/libk5crypto.so.3.1
7f45b31a5000-7f45b31a6000 rw-p 00000000 00:00 0
7f45b31a6000-7f45b31c0000 r-xp 00000000 08:01 1179687                    /lib/x86_64-linux-gnu/libpthread-2.27.so
7f45b31c0000-7f45b33bf000 ---p 0001a000 08:01 1179687                    /lib/x86_64-linux-gnu/libpthread-2.27.so
7f45b33bf000-7f45b33c0000 r--p 00019000 08:01 1179687                    /lib/x86_64-linux-gnu/libpthread-2.27.so
7f45b33c0000-7f45b33c1000 rw-p 0001a000 08:01 1179687                    /lib/x86_64-linux-gnu/libpthread-2.27.so
7f45b33c1000-7f45b33c5000 rw-p 00000000 00:00 0
7f45b33c5000-7f45b34d9000 r-xp 00000000 08:01 1179818                    /lib/x86_64-linux-gnu/libgcrypt.so.20.2.1
7f45b34d9000-7f45b36d9000 ---p 00114000 08:01 1179818                    /lib/x86_64-linux-gnu/libgcrypt.so.20.2.1
7f45b36d9000-7f45b36db000 r--p 00114000 08:01 1179818                    /lib/x86_64-linux-gnu/libgcrypt.so.20.2.1
7f45b36db000-7f45b36e0000 rw-p 00116000 08:01 1179818                    /lib/x86_64-linux-gnu/libgcrypt.so.20.2.1
7f45b36e0000-7f45b36e1000 rw-p 00000000 00:00 0
7f45b36e1000-7f45b36fc000 r-xp 00000000 08:01 1311361                    /usr/lib/x86_64-linux-gnu/liblz4.so.1.7.1
7f45b36fc000-7f45b38fb000 ---p 0001b000 08:01 1311361                    /usr/lib/x86_64-linux-gnu/liblz4.so.1.7.1
7f45b38fb000-7f45b38fc000 r--p 0001a000 08:01 1311361                    /usr/lib/x86_64-linux-gnu/liblz4.so.1.7.1
7f45b38fc000-7f45b38fd000 rw-p 0001b000 08:01 1311361                    /usr/lib/x86_64-linux-gnu/liblz4.so.1.7.1
7f45b38fd000-7f45b3921000 r-xp 00000000 08:01 1179716                    /lib/x86_64-linux-gnu/liblzma.so.5.2.2
7f45b3921000-7f45b3b21000 ---p 00024000 08:01 1179716                    /lib/x86_64-linux-gnu/liblzma.so.5.2.2
7f45b3b21000-7f45b3b22000 r--p 00024000 08:01 1179716                    /lib/x86_64-linux-gnu/liblzma.so.5.2.2
7f45b3b22000-7f45b3b23000 rw-p 00025000 08:01 1179716                    /lib/x86_64-linux-gnu/liblzma.so.5.2.2
7f45b3b23000-7f45b3b2a000 r-xp 00000000 08:01 1179689                    /lib/x86_64-linux-gnu/librt-2.27.so
7f45b3b2a000-7f45b3d29000 ---p 00007000 08:01 1179689                    /lib/x86_64-linux-gnu/librt-2.27.so
7f45b3d29000-7f45b3d2a000 r--p 00006000 08:01 1179689                    /lib/x86_64-linux-gnu/librt-2.27.so
7f45b3d2a000-7f45b3d2b000 rw-p 00007000 08:01 1179689                    /lib/x86_64-linux-gnu/librt-2.27.so
7f45b3d2b000-7f45b3d9b000 r-xp 00000000 08:01 1179739                    /lib/x86_64-linux-gnu/libpcre.so.3.13.3
7f45b3d9b000-7f45b3f9b000 ---p 00070000 08:01 1179739                    /lib/x86_64-linux-gnu/libpcre.so.3.13.3
7f45b3f9b000-7f45b3f9c000 r--p 00070000 08:01 1179739                    /lib/x86_64-linux-gnu/libpcre.so.3.13.3
7f45b3f9c000-7f45b3f9d000 rw-p 00071000 08:01 1179739                    /lib/x86_64-linux-gnu/libpcre.so.3.13.3
7f45b3f9d000-7f45b3fa0000 r-xp 00000000 08:01 1179675                    /lib/x86_64-linux-gnu/libdl-2.27.so
7f45b3fa0000-7f45b419f000 ---p 00003000 08:01 1179675                    /lib/x86_64-linux-gnu/libdl-2.27.so
7f45b419f000-7f45b41a0000 r--p 00002000 08:01 1179675                    /lib/x86_64-linux-gnu/libdl-2.27.so
7f45b41a0000-7f45b41a1000 rw-p 00003000 08:01 1179675                    /lib/x86_64-linux-gnu/libdl-2.27.so
7f45b41a1000-7f45b41a5000 r-xp 00000000 08:01 1179653                    /lib/x86_64-linux-gnu/libcap-ng.so.0.0.0
7f45b41a5000-7f45b43a4000 ---p 00004000 08:01 1179653                    /lib/x86_64-linux-gnu/libcap-ng.so.0.0.0
7f45b43a4000-7f45b43a5000 r--p 00003000 08:01 1179653                    /lib/x86_64-linux-gnu/libcap-ng.so.0.0.0
7f45b43a5000-7f45b43a6000 rw-p 00004000 08:01 1179653                    /lib/x86_64-linux-gnu/libcap-ng.so.0.0.0
7f45b43a6000-7f45b43bd000 r-xp 00000000 08:01 1179679                    /lib/x86_64-linux-gnu/libnsl-2.27.so
7f45b43bd000-7f45b45bc000 ---p 00017000 08:01 1179679                    /lib/x86_64-linux-gnu/libnsl-2.27.so
7f45b45bc000-7f45b45bd000 r--p 00016000 08:01 1179679                    /lib/x86_64-linux-gnu/libnsl-2.27.so
7f45b45bd000-7f45b45be000 rw-p 00017000 08:01 1179679                    /lib/x86_64-linux-gnu/libnsl-2.27.so
7f45b45be000-7f45b45c0000 rw-p 00000000 00:00 0
7f45b45c0000-7f45b47a7000 r-xp 00000000 08:01 1179672                    /lib/x86_64-linux-gnu/libc-2.27.so
7f45b47a7000-7f45b49a7000 ---p 001e7000 08:01 1179672                    /lib/x86_64-linux-gnu/libc-2.27.so
7f45b49a7000-7f45b49ab000 r--p 001e7000 08:01 1179672                    /lib/x86_64-linux-gnu/libc-2.27.so
7f45b49ab000-7f45b49ad000 rw-p 001eb000 08:01 1179672                    /lib/x86_64-linux-gnu/libc-2.27.so
7f45b49ad000-7f45b49b1000 rw-p 00000000 00:00 0
7f45b49b1000-7f45b49b4000 r-xp 00000000 08:01 1179853                    /lib/x86_64-linux-gnu/libcom_err.so.2.1
7f45b49b4000-7f45b4bb3000 ---p 00003000 08:01 1179853                    /lib/x86_64-linux-gnu/libcom_err.so.2.1
7f45b4bb3000-7f45b4bb4000 r--p 00002000 08:01 1179853                    /lib/x86_64-linux-gnu/libcom_err.so.2.1
7f45b4bb4000-7f45b4bb5000 rw-p 00003000 08:01 1179853                    /lib/x86_64-linux-gnu/libcom_err.so.2.1
7f45b4bb5000-7f45b4c7b000 r-xp 00000000 08:01 1321208                    /usr/lib/x86_64-linux-gnu/libkrb5.so.3.3
7f45b4c7b000-7f45b4e7b000 ---p 000c6000 08:01 1321208                    /usr/lib/x86_64-linux-gnu/libkrb5.so.3.3
7f45b4e7b000-7f45b4e89000 r--p 000c6000 08:01 1321208                    /usr/lib/x86_64-linux-gnu/libkrb5.so.3.3
7f45b4e89000-7f45b4e8b000 rw-p 000d4000 08:01 1321208                    /usr/lib/x86_64-linux-gnu/libkrb5.so.3.3
7f45b4e8b000-7f45b4ed3000 r-xp 00000000 08:01 1321211                    /usr/lib/x86_64-linux-gnu/libgssapi_krb5.so.2.2
7f45b4ed3000-7f45b50d2000 ---p 00048000 08:01 1321211                    /usr/lib/x86_64-linux-gnu/libgssapi_krb5.so.2.2
7f45b50d2000-7f45b50d4000 r--p 00047000 08:01 1321211                    /usr/lib/x86_64-linux-gnu/libgssapi_krb5.so.2.2
7f45b50d4000-7f45b50d6000 rw-p 00049000 08:01 1321211                    /usr/lib/x86_64-linux-gnu/libgssapi_krb5.so.2.2
7f45b50d6000-7f45b50df000 r-xp 00000000 08:01 1179674                    /lib/x86_64-linux-gnu/libcrypt-2.27.so
7f45b50df000-7f45b52de000 ---p 00009000 08:01 1179674                    /lib/x86_64-linux-gnu/libcrypt-2.27.so
7f45b52de000-7f45b52df000 r--p 00008000 08:01 1179674                    /lib/x86_64-linux-gnu/libcrypt-2.27.so
7f45b52df000-7f45b52e0000 rw-p 00009000 08:01 1179674                    /lib/x86_64-linux-gnu/libcrypt-2.27.so
7f45b52e0000-7f45b530e000 rw-p 00000000 00:00 0
7f45b530e000-7f45b532a000 r-xp 00000000 08:01 1179815                    /lib/x86_64-linux-gnu/libz.so.1.2.11
7f45b532a000-7f45b5529000 ---p 0001c000 08:01 1179815                    /lib/x86_64-linux-gnu/libz.so.1.2.11
7f45b5529000-7f45b552a000 r--p 0001b000 08:01 1179815                    /lib/x86_64-linux-gnu/libz.so.1.2.11
7f45b552a000-7f45b552b000 rw-p 0001c000 08:01 1179815                    /lib/x86_64-linux-gnu/libz.so.1.2.11
7f45b552b000-7f45b552d000 r-xp 00000000 08:01 1179691                    /lib/x86_64-linux-gnu/libutil-2.27.so
7f45b552d000-7f45b572c000 ---p 00002000 08:01 1179691                    /lib/x86_64-linux-gnu/libutil-2.27.so
7f45b572c000-7f45b572d000 r--p 00001000 08:01 1179691                    /lib/x86_64-linux-gnu/libutil-2.27.so
7f45b572d000-7f45b572e000 rw-p 00002000 08:01 1179691                    /lib/x86_64-linux-gnu/libutil-2.27.so
7f45b572e000-7f45b5947000 r-xp 00000000 08:01 1321482                    /usr/lib/x86_64-linux-gnu/libcrypto.so.1.0.0
7f45b5947000-7f45b5b46000 ---p 00219000 08:01 1321482                    /usr/lib/x86_64-linux-gnu/libcrypto.so.1.0.0
7f45b5b46000-7f45b5b62000 r--p 00218000 08:01 1321482                    /usr/lib/x86_64-linux-gnu/libcrypto.so.1.0.0
7f45b5b62000-7f45b5b6e000 rw-p 00234000 08:01 1321482                    /usr/lib/x86_64-linux-gnu/libcrypto.so.1.0.0
7f45b5b6e000-7f45b5b71000 rw-p 00000000 00:00 0
7f45b5b71000-7f45b5bf1000 r-xp 00000000 08:01 1179838                    /lib/x86_64-linux-gnu/libsystemd.so.0.21.0
7f45b5bf1000-7f45b5df0000 ---p 00080000 08:01 1179838                    /lib/x86_64-linux-gnu/libsystemd.so.0.21.0
7f45b5df0000-7f45b5df3000 r--p 0007f000 08:01 1179838                    /lib/x86_64-linux-gnu/libsystemd.so.0.21.0
7f45b5df3000-7f45b5df4000 rw-p 00082000 08:01 1179838                    /lib/x86_64-linux-gnu/libsystemd.so.0.21.0
7f45b5df4000-7f45b5df5000 rw-p 00000000 00:00 0
7f45b5df5000-7f45b5e1a000 r-xp 00000000 08:01 1179745                    /lib/x86_64-linux-gnu/libselinux.so.1
7f45b5e1a000-7f45b6019000 ---p 00025000 08:01 1179745                    /lib/x86_64-linux-gnu/libselinux.so.1
7f45b6019000-7f45b601a000 r--p 00024000 08:01 1179745                    /lib/x86_64-linux-gnu/libselinux.so.1
7f45b601a000-7f45b601b000 rw-p 00025000 08:01 1179745                    /lib/x86_64-linux-gnu/libselinux.so.1
7f45b601b000-7f45b601d000 rw-p 00000000 00:00 0
7f45b601d000-7f45b602a000 r-xp 00000000 08:01 1179671                    /lib/x86_64-linux-gnu/libpam.so.0.83.1
7f45b602a000-7f45b6229000 ---p 0000d000 08:01 1179671                    /lib/x86_64-linux-gnu/libpam.so.0.83.1
7f45b6229000-7f45b622a000 r--p 0000c000 08:01 1179671                    /lib/x86_64-linux-gnu/libpam.so.0.83.1
7f45b622a000-7f45b622b000 rw-p 0000d000 08:01 1179671                    /lib/x86_64-linux-gnu/libpam.so.0.83.1
7f45b622b000-7f45b6248000 r-xp 00000000 08:01 1179657                    /lib/x86_64-linux-gnu/libaudit.so.1.0.0
7f45b6248000-7f45b6448000 ---p 0001d000 08:01 1179657                    /lib/x86_64-linux-gnu/libaudit.so.1.0.0
7f45b6448000-7f45b6449000 r--p 0001d000 08:01 1179657                    /lib/x86_64-linux-gnu/libaudit.so.1.0.0
7f45b6449000-7f45b644a000 rw-p 0001e000 08:01 1179657                    /lib/x86_64-linux-gnu/libaudit.so.1.0.0
7f45b644a000-7f45b6454000 rw-p 00000000 00:00 0
7f45b6454000-7f45b645c000 r-xp 00000000 08:01 1180009                    /lib/x86_64-linux-gnu/libwrap.so.0.7.6
7f45b645c000-7f45b665c000 ---p 00008000 08:01 1180009                    /lib/x86_64-linux-gnu/libwrap.so.0.7.6
7f45b665c000-7f45b665d000 r--p 00008000 08:01 1180009                    /lib/x86_64-linux-gnu/libwrap.so.0.7.6
7f45b665d000-7f45b665e000 rw-p 00009000 08:01 1180009                    /lib/x86_64-linux-gnu/libwrap.so.0.7.6
7f45b665e000-7f45b6685000 r-xp 00000000 08:01 1179663                    /lib/x86_64-linux-gnu/ld-2.27.so
7f45b686b000-7f45b687a000 rw-p 00000000 00:00 0
7f45b6885000-7f45b6886000 r--p 00027000 08:01 1179663                    /lib/x86_64-linux-gnu/ld-2.27.so
7f45b6886000-7f45b6887000 rw-p 00028000 08:01 1179663                    /lib/x86_64-linux-gnu/ld-2.27.so
7f45b6887000-7f45b6888000 rw-p 00000000 00:00 0
7ffeb6459000-7ffeb647a000 rw-p 00000000 00:00 0                          [stack]
7ffeb65b2000-7ffeb65b5000 r--p 00000000 00:00 0                          [vvar]
7ffeb65b5000-7ffeb65b7000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]
[wroathe@rohan:~] $
```
