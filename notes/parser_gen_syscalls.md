```
[wroathe@rohan:parser_gen] (master) $ strace ./parser_gen --type=lr1 --spec examples/spec_file.pspec examples/spec_file.pspec
execve("./parser_gen", ["./parser_gen", "--type=lr1", "--spec", "examples/spec_file.pspec", "examples/spec_file.pspec"], 0x7ffe5e249540 /* 24 vars */) = 0
brk(NULL)                               = 0x55eba7bde000
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/wroathe/lib/tls/x86_64/x86_64/libbase.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/home/wroathe/lib/tls/x86_64/x86_64", 0x7ffea66d5310) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/wroathe/lib/tls/x86_64/libbase.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/home/wroathe/lib/tls/x86_64", 0x7ffea66d5310) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/wroathe/lib/tls/x86_64/libbase.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/home/wroathe/lib/tls/x86_64", 0x7ffea66d5310) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/wroathe/lib/tls/libbase.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/home/wroathe/lib/tls", 0x7ffea66d5310) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/wroathe/lib/x86_64/x86_64/libbase.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/home/wroathe/lib/x86_64/x86_64", 0x7ffea66d5310) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/wroathe/lib/x86_64/libbase.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/home/wroathe/lib/x86_64", 0x7ffea66d5310) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/wroathe/lib/x86_64/libbase.so", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
stat("/home/wroathe/lib/x86_64", 0x7ffea66d5310) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/home/wroathe/lib/libbase.so", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\360;\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0775, st_size=133888, ...}) = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fa90a481000
mmap(NULL, 2159640, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fa90a04c000
mprotect(0x7fa90a05b000, 2093056, PROT_NONE) = 0
mmap(0x7fa90a25a000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xe000) = 0x7fa90a25a000
close(3)                                = 0
openat(AT_FDCWD, "/home/wroathe/lib/libgram.so", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\3206\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0775, st_size=224576, ...}) = 0
mmap(NULL, 2221576, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fa909e2d000
mprotect(0x7fa909e46000, 2097152, PROT_NONE) = 0
mmap(0x7fa90a046000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x19000) = 0x7fa90a046000
mmap(0x7fa90a048000, 13832, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7fa90a048000
close(3)                                = 0
openat(AT_FDCWD, "/home/wroathe/lib/libc.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=44635, ...}) = 0
mmap(NULL, 44635, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7fa90a476000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\260\34\2\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=2030544, ...}) = 0
mmap(NULL, 4131552, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fa909a3c000
mprotect(0x7fa909c23000, 2097152, PROT_NONE) = 0
mmap(0x7fa909e23000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1e7000) = 0x7fa909e23000
mmap(0x7fa909e29000, 15072, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7fa909e29000
close(3)                                = 0
openat(AT_FDCWD, "/home/wroathe/lib/libcgraph.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/libcgraph.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\340?\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=89560, ...}) = 0
mmap(NULL, 2185608, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fa909826000
mprotect(0x7fa90983a000, 2097152, PROT_NONE) = 0
mmap(0x7fa909a3a000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x14000) = 0x7fa909a3a000
close(3)                                = 0
openat(AT_FDCWD, "/home/wroathe/lib/libm.so.6", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libm.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\200\272\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=1700792, ...}) = 0
mmap(NULL, 3789144, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fa909488000
mprotect(0x7fa909625000, 2093056, PROT_NONE) = 0
mmap(0x7fa909824000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x19c000) = 0x7fa909824000
close(3)                                = 0
openat(AT_FDCWD, "/home/wroathe/lib/libregex.so", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\360$\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0775, st_size=107312, ...}) = 0
mmap(NULL, 2177320, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fa909274000
mprotect(0x7fa909280000, 2097152, PROT_NONE) = 0
mmap(0x7fa909480000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xc000) = 0x7fa909480000
mmap(0x7fa909482000, 22824, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7fa909482000
close(3)                                = 0
openat(AT_FDCWD, "/home/wroathe/lib/libcdt.so.5", O_RDONLY|O_CLOEXEC) = -1 ENOENT (No such file or directory)
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/usr/lib/x86_64-linux-gnu/libcdt.so.5", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0`\r\0\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0644, st_size=26792, ...}) = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fa90a474000
mmap(NULL, 2122088, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fa90906d000
mprotect(0x7fa909072000, 2097152, PROT_NONE) = 0
mmap(0x7fa909272000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x5000) = 0x7fa909272000
close(3)                                = 0
mmap(NULL, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fa90a471000
arch_prctl(ARCH_SET_FS, 0x7fa90a471740) = 0
mprotect(0x7fa909e23000, 16384, PROT_READ) = 0
mprotect(0x7fa909272000, 4096, PROT_READ) = 0
mprotect(0x7fa909a3a000, 4096, PROT_READ) = 0
mprotect(0x7fa909824000, 4096, PROT_READ) = 0
mprotect(0x7fa90a25a000, 4096, PROT_READ) = 0
mprotect(0x7fa909480000, 4096, PROT_READ) = 0
mprotect(0x7fa90a046000, 4096, PROT_READ) = 0
mprotect(0x55eba7489000, 4096, PROT_READ) = 0
mprotect(0x7fa90a483000, 4096, PROT_READ) = 0
munmap(0x7fa90a476000, 44635)           = 0
brk(NULL)                               = 0x55eba7bde000
brk(0x55eba7bff000)                     = 0x55eba7bff000
openat(AT_FDCWD, "examples/spec_file.pspec", O_RDONLY) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=568, ...}) = 0
read(3, "# comment\n\n-line_comment   /#[^\\"..., 49152) = 568
read(3, "", 49152)                      = 0
close(3)                                = 0
openat(AT_FDCWD, "examples/spec_file.pspec", O_RDONLY) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=568, ...}) = 0
read(3, "# comment\n\n-line_comment   /#[^\\"..., 49152) = 568
read(3, "", 49152)                      = 0
close(3)                                = 0
fstat(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 0), ...}) = 0
write(1, "filename: examples/spec_file.psp"..., 46filename: examples/spec_file.pspec, size: 568
) = 46
write(1, "parsed pdef_mod\n", 16parsed pdef_mod
)       = 16
write(1, "parsed pattern_def\n", 19parsed pattern_def
)    = 19
write(1, "parsed pdef_mod\n", 16parsed pdef_mod
)       = 16
write(1, "parsed pattern_def\n", 19parsed pattern_def
)    = 19
write(1, "parsed pdef_mod\n", 16parsed pdef_mod
)       = 16
write(1, "parsed pattern_def\n", 19parsed pattern_def
)    = 19
write(1, "parsed pdef_mod\n", 16parsed pdef_mod
)       = 16
write(1, "parsed pattern_def\n", 19parsed pattern_def
)    = 19
write(1, "parsed pdef_mod\n", 16parsed pdef_mod
)       = 16
write(1, "parsed pattern_def\n", 19parsed pattern_def
)    = 19
write(1, "parsed pattern_defs\n", 20parsed pattern_defs
)   = 20
write(1, "parsed pattern_defs\n", 20parsed pattern_defs
)   = 20
write(1, "parsed pattern_defs\n", 20parsed pattern_defs
)   = 20
write(1, "parsed pattern_defs\n", 20parsed pattern_defs
)   = 20
write(1, "parsed pattern_defs\n", 20parsed pattern_defs
)   = 20
write(1, "parsed pattern_defs\n", 20parsed pattern_defs
)   = 20
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed alt\n", 11parsed alt
)            = 11
write(1, "parsed alts\n", 12parsed alts
)           = 12
write(1, "parsed rule\n", 12parsed rule
)           = 12
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed alt\n", 11parsed alt
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed alt\n", 11parsed alt
)            = 11
write(1, "parsed alts\n", 12parsed alts
)           = 12
write(1, "parsed alts\n", 12parsed alts
)           = 12
write(1, "parsed rule\n", 12parsed rule
)           = 12
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed alt\n", 11parsed alt
)            = 11
write(1, "parsed alts\n", 12parsed alts
)           = 12
write(1, "parsed rule\n", 12parsed rule
)           = 12
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed alt\n", 11parsed alt
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed alt\n", 11parsed alt
)            = 11
write(1, "parsed alts\n", 12parsed alts
)           = 12
write(1, "parsed alts\n", 12parsed alts
)           = 12
write(1, "parsed rule\n", 12parsed rule
)           = 12
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed alt\n", 11parsed alt
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed alt\n", 11parsed alt
)            = 11
write(1, "parsed alts\n", 12parsed alts
)           = 12
write(1, "parsed alts\n", 12parsed alts
)           = 12
write(1, "parsed rule\n", 12parsed rule
)           = 12
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed alt\n", 11parsed alt
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed alt\n", 11parsed alt
)            = 11
write(1, "parsed alts\n", 12parsed alts
)           = 12
write(1, "parsed alts\n", 12parsed alts
)           = 12
write(1, "parsed rule\n", 12parsed rule
)           = 12
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed alt\n", 11parsed alt
)            = 11
write(1, "parsed alts\n", 12parsed alts
)           = 12
write(1, "parsed rule\n", 12parsed rule
)           = 12
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed alt\n", 11parsed alt
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed alt\n", 11parsed alt
)            = 11
write(1, "parsed alts\n", 12parsed alts
)           = 12
write(1, "parsed alts\n", 12parsed alts
)           = 12
write(1, "parsed rule\n", 12parsed rule
)           = 12
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed alt\n", 11parsed alt
)            = 11
write(1, "parsed alts\n", 12parsed alts
)           = 12
write(1, "parsed rule\n", 12parsed rule
)           = 12
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed alt\n", 11parsed alt
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed alt\n", 11parsed alt
)            = 11
write(1, "parsed alts\n", 12parsed alts
)           = 12
write(1, "parsed alts\n", 12parsed alts
)           = 12
write(1, "parsed rule\n", 12parsed rule
)           = 12
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed alt\n", 11parsed alt
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed alt\n", 11parsed alt
)            = 11
write(1, "parsed rhs\n", 11parsed rhs
)            = 11
write(1, "parsed rhses\n", 13parsed rhses
)          = 13
write(1, "parsed alt\n", 11parsed alt
)            = 11
write(1, "parsed alts\n", 12parsed alts
)           = 12
write(1, "parsed alts\n", 12parsed alts
)           = 12
write(1, "parsed alts\n", 12parsed alts
)           = 12
write(1, "parsed rule\n", 12parsed rule
)           = 12
write(1, "parsed rules\n", 13parsed rules
)          = 13
write(1, "parsed rules\n", 13parsed rules
)          = 13
write(1, "parsed rules\n", 13parsed rules
)          = 13
write(1, "parsed rules\n", 13parsed rules
)          = 13
write(1, "parsed rules\n", 13parsed rules
)          = 13
write(1, "parsed rules\n", 13parsed rules
)          = 13
write(1, "parsed rules\n", 13parsed rules
)          = 13
write(1, "parsed rules\n", 13parsed rules
)          = 13
write(1, "parsed rules\n", 13parsed rules
)          = 13
write(1, "parsed rules\n", 13parsed rules
)          = 13
write(1, "parsed rules\n", 13parsed rules
)          = 13
write(1, "parsed rules\n", 13parsed rules
)          = 13
write(1, "parsed grammar\n", 15parsed grammar
)        = 15
write(1, "parsed parser_spec\n", 19parsed parser_spec
)    = 19
write(1, "parsed examples/spec_file.pspec\n", 32parsed examples/spec_file.pspec
) = 32
exit_group(0)                           = ?
+++ exited with 0 +++
```

```
mmap(0x7fa90a25a000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xe000) = 0x7fa90a25a000
mmap(NULL, 2221576, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fa909e2d000
mprotect(0x7fa909e46000, 2097152, PROT_NONE) = 0
mmap(0x7fa90a046000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x19000) = 0x7fa90a046000
mmap(0x7fa90a048000, 13832, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7fa90a048000
mmap(NULL, 44635, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7fa90a476000
mmap(NULL, 4131552, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fa909a3c000
mprotect(0x7fa909c23000, 2097152, PROT_NONE) = 0
mmap(0x7fa909e23000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1e7000) = 0x7fa909e23000
mmap(0x7fa909e29000, 15072, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7fa909e29000
mmap(NULL, 2185608, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fa909826000
mprotect(0x7fa90983a000, 2097152, PROT_NONE) = 0
mmap(0x7fa909a3a000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x14000) = 0x7fa909a3a000
mmap(NULL, 3789144, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fa909488000
mprotect(0x7fa909625000, 2093056, PROT_NONE) = 0
mmap(0x7fa909824000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x19c000) = 0x7fa909824000
mmap(NULL, 2177320, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fa909274000
mprotect(0x7fa909280000, 2097152, PROT_NONE) = 0
mmap(0x7fa909480000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0xc000) = 0x7fa909480000
mmap(0x7fa909482000, 22824, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7fa909482000
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fa90a474000
mmap(NULL, 2122088, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fa90906d000
mprotect(0x7fa909072000, 2097152, PROT_NONE) = 0
mmap(0x7fa909272000, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x5000) = 0x7fa909272000
mmap(NULL, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fa90a471000
mprotect(0x7fa909e23000, 16384, PROT_READ) = 0
mprotect(0x7fa909272000, 4096, PROT_READ) = 0
mprotect(0x7fa909a3a000, 4096, PROT_READ) = 0
mprotect(0x7fa909824000, 4096, PROT_READ) = 0
mprotect(0x7fa90a25a000, 4096, PROT_READ) = 0
mprotect(0x7fa909480000, 4096, PROT_READ) = 0
mprotect(0x7fa90a046000, 4096, PROT_READ) = 0
mprotect(0x55eba7489000, 4096, PROT_READ) = 0
mprotect(0x7fa90a483000, 4096, PROT_READ) = 0
```
   
```
See:
https://github.com/torvalds/linux/blob/9ff7258575d5fee011649d20cc56de720a395191/Documentation/filesystems/proc.rst

(size) address           perms offset  dev   inode      pathname
  ^ 
  | added by me

-rwxrwxr-x 1 wroathe wroathe   45264 Jul  3 14:32 /home/wroathe/compilers/src/parser_gen/parser_gen
-rwxrwxr-x 1 wroathe wroathe  133888 Jul  2 12:41 /home/wroathe/lib/libbase.so
-rwxrwxr-x 1 wroathe wroathe  224576 Jul  2 12:41 /home/wroathe/lib/libgram.so
-rwxrwxr-x 1 wroathe wroathe  107312 Jul  2 12:41 /home/wroathe/lib/libregex.so
-rwxr-xr-x 1 root    root     170960 Apr 16  2018 /lib/x86_64-linux-gnu/ld-2.27.so
-rw-r--r-- 1 root    root    1700792 Apr 16  2018 /lib/x86_64-linux-gnu/libm-2.27.so
-rw-r--r-- 1 root    root      26792 Mar 24  2018 /usr/lib/x86_64-linux-gnu/libcdt.so.5.0.0
-rw-r--r-- 1 root    root      89560 Mar 24  2018 /usr/lib/x86_64-linux-gnu/libcgraph.so.6.0.0

[wroathe@rohan:parser_gen] (master) $ sudo cat /proc/1040/maps
20480       55a9a1ce8000-55a9a1ced000 r-xp 00000000 08:01 1069186                    /home/wroathe/compilers/src/parser_gen/parser_gen
4096        55a9a1eec000-55a9a1eed000 r--p 00004000 08:01 1069186                    /home/wroathe/compilers/src/parser_gen/parser_gen
4096        55a9a1eed000-55a9a1eee000 rw-p 00005000 08:01 1069186                    /home/wroathe/compilers/src/parser_gen/parser_gen
135168      55a9a2c67000-55a9a2c88000 rw-p 00000000 00:00 0                          [heap]
20480       7f057296e000-7f0572973000 r-xp 00000000 08:01 1317687                    /usr/lib/x86_64-linux-gnu/libcdt.so.5.0.0
2097152     7f0572973000-7f0572b73000 ---p 00005000 08:01 1317687                    /usr/lib/x86_64-linux-gnu/libcdt.so.5.0.0
4096        7f0572b73000-7f0572b74000 r--p 00005000 08:01 1317687                    /usr/lib/x86_64-linux-gnu/libcdt.so.5.0.0
4096        7f0572b74000-7f0572b75000 rw-p 00006000 08:01 1317687                    /usr/lib/x86_64-linux-gnu/libcdt.so.5.0.0
49152       7f0572b75000-7f0572b81000 r-xp 00000000 08:01 1069191                    /home/wroathe/compilers/libs/regex/libregex.so
2097152     7f0572b81000-7f0572d81000 ---p 0000c000 08:01 1069191                    /home/wroathe/compilers/libs/regex/libregex.so
4096        7f0572d81000-7f0572d82000 r--p 0000c000 08:01 1069191                    /home/wroathe/compilers/libs/regex/libregex.so
4096        7f0572d82000-7f0572d83000 rw-p 0000d000 08:01 1069191                    /home/wroathe/compilers/libs/regex/libregex.so
24576       7f0572d83000-7f0572d89000 rw-p 00000000 00:00 0
1691648     7f0572d89000-7f0572f26000 r-xp 00000000 08:01 1179676                    /lib/x86_64-linux-gnu/libm-2.27.so
2093056     7f0572f26000-7f0573125000 ---p 0019d000 08:01 1179676                    /lib/x86_64-linux-gnu/libm-2.27.so
4096        7f0573125000-7f0573126000 r--p 0019c000 08:01 1179676                    /lib/x86_64-linux-gnu/libm-2.27.so
4096        7f0573126000-7f0573127000 rw-p 0019d000 08:01 1179676                    /lib/x86_64-linux-gnu/libm-2.27.so
81920       7f0573127000-7f057313b000 r-xp 00000000 08:01 1317689                    /usr/lib/x86_64-linux-gnu/libcgraph.so.6.0.0
2097152     7f057313b000-7f057333b000 ---p 00014000 08:01 1317689                    /usr/lib/x86_64-linux-gnu/libcgraph.so.6.0.0
4096        7f057333b000-7f057333c000 r--p 00014000 08:01 1317689                    /usr/lib/x86_64-linux-gnu/libcgraph.so.6.0.0
4096        7f057333c000-7f057333d000 rw-p 00015000 08:01 1317689                    /usr/lib/x86_64-linux-gnu/libcgraph.so.6.0.0
1994752     7f057333d000-7f0573524000 r-xp 00000000 08:01 1179672                    /lib/x86_64-linux-gnu/libc-2.27.so
2097152     7f0573524000-7f0573724000 ---p 001e7000 08:01 1179672                    /lib/x86_64-linux-gnu/libc-2.27.so
16384       7f0573724000-7f0573728000 r--p 001e7000 08:01 1179672                    /lib/x86_64-linux-gnu/libc-2.27.so
8192        7f0573728000-7f057372a000 rw-p 001eb000 08:01 1179672                    /lib/x86_64-linux-gnu/libc-2.27.so
16384       7f057372a000-7f057372e000 rw-p 00000000 00:00 0
102400      7f057372e000-7f0573747000 r-xp 00000000 08:01 1069242                    /home/wroathe/compilers/libs/gram/libgram.so
2097152     7f0573747000-7f0573947000 ---p 00019000 08:01 1069242                    /home/wroathe/compilers/libs/gram/libgram.so
4096        7f0573947000-7f0573948000 r--p 00019000 08:01 1069242                    /home/wroathe/compilers/libs/gram/libgram.so
4096        7f0573948000-7f0573949000 rw-p 0001a000 08:01 1069242                    /home/wroathe/compilers/libs/gram/libgram.so
16384       7f0573949000-7f057394d000 rw-p 00000000 00:00 0
61440       7f057394d000-7f057395c000 r-xp 00000000 08:01 1069251                    /home/wroathe/compilers/libs/base/libbase.so
2093056     7f057395c000-7f0573b5b000 ---p 0000f000 08:01 1069251                    /home/wroathe/compilers/libs/base/libbase.so
4096        7f0573b5b000-7f0573b5c000 r--p 0000e000 08:01 1069251                    /home/wroathe/compilers/libs/base/libbase.so
4096        7f0573b5c000-7f0573b5d000 rw-p 0000f000 08:01 1069251                    /home/wroathe/compilers/libs/base/libbase.so
159744      7f0573b5d000-7f0573b84000 r-xp 00000000 08:01 1179663                    /lib/x86_64-linux-gnu/ld-2.27.so
20480       7f0573d72000-7f0573d77000 rw-p 00000000 00:00 0
8192        7f0573d82000-7f0573d84000 rw-p 00000000 00:00 0
4096        7f0573d84000-7f0573d85000 r--p 00027000 08:01 1179663                    /lib/x86_64-linux-gnu/ld-2.27.so
4096        7f0573d85000-7f0573d86000 rw-p 00028000 08:01 1179663                    /lib/x86_64-linux-gnu/ld-2.27.so
4096        7f0573d86000-7f0573d87000 rw-p 00000000 00:00 0
278528      7ffe9a93a000-7ffe9a97e000 rw-p 00000000 00:00 0                          [stack]
12288       7ffe9a9a9000-7ffe9a9ac000 r--p 00000000 00:00 0                          [vvar]
8192        7ffe9a9ac000-7ffe9a9ae000 r-xp 00000000 00:00 0                          [vdso]
    ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]
```

```
[wroathe@rohan:~] $ sudo cat /proc/1129/status
Name:	parser_gen
Umask:	0002
State:	S (sleeping)
Tgid:	1129
Ngid:	0
Pid:	1129
PPid:	1
TracerPid:	0
Uid:	1000	1000	1000	1000
Gid:	1000	1000	1000	1000
FDSize:	256
Groups:	4 24 27 30 46 111 112 1000
NStgid:	1129
NSpid:	1129
NSpgid:	1129
NSsid:	1083
VmPeak:	   19012 kB
VmSize:	   19012 kB
VmLck:	       0 kB
VmPin:	       0 kB
VmHWM:	    2256 kB
VmRSS:	    2256 kB
RssAnon:	     344 kB
RssFile:	    1912 kB
RssShmem:	       0 kB
VmData:	     260 kB
VmStk:	     272 kB
VmExe:	      20 kB
VmLib:	    4072 kB
VmPTE:	      76 kB
VmSwap:	       0 kB
HugetlbPages:	       0 kB
CoreDumping:	0
Threads:	1
SigQ:	0/7809
SigPnd:	0000000000000000
ShdPnd:	0000000000000000
SigBlk:	0000000000000000
SigIgn:	0000000000000000
SigCgt:	0000000000000000
CapInh:	0000000000000000
CapPrm:	0000000000000000
CapEff:	0000000000000000
CapBnd:	0000003fffffffff
CapAmb:	0000000000000000
NoNewPrivs:	0
Seccomp:	0
Speculation_Store_Bypass:	vulnerable
Cpus_allowed:	3
Cpus_allowed_list:	0-1
Mems_allowed:	00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000001
Mems_allowed_list:	0
voluntary_ctxt_switches:	1
nonvoluntary_ctxt_switches:	10

Two Separate Invocations:

[wroathe@rohan:~] $ sudo cat /proc/1129/maps
56528561f000-565285624000 r-xp 00000000 08:01 1069186                    /home/wroathe/compilers/src/parser_gen/parser_gen
565285823000-565285824000 r--p 00004000 08:01 1069186                    /home/wroathe/compilers/src/parser_gen/parser_gen
565285824000-565285825000 rw-p 00005000 08:01 1069186                    /home/wroathe/compilers/src/parser_gen/parser_gen
565286cfd000-565286d1e000 rw-p 00000000 00:00 0                          [heap]
7fe202293000-7fe202298000 r-xp 00000000 08:01 1317687                    /usr/lib/x86_64-linux-gnu/libcdt.so.5.0.0
7fe202298000-7fe202498000 ---p 00005000 08:01 1317687                    /usr/lib/x86_64-linux-gnu/libcdt.so.5.0.0
7fe202498000-7fe202499000 r--p 00005000 08:01 1317687                    /usr/lib/x86_64-linux-gnu/libcdt.so.5.0.0
7fe202499000-7fe20249a000 rw-p 00006000 08:01 1317687                    /usr/lib/x86_64-linux-gnu/libcdt.so.5.0.0
7fe20249a000-7fe2024a6000 r-xp 00000000 08:01 1069191                    /home/wroathe/compilers/libs/regex/libregex.so
7fe2024a6000-7fe2026a6000 ---p 0000c000 08:01 1069191                    /home/wroathe/compilers/libs/regex/libregex.so
7fe2026a6000-7fe2026a7000 r--p 0000c000 08:01 1069191                    /home/wroathe/compilers/libs/regex/libregex.so
7fe2026a7000-7fe2026a8000 rw-p 0000d000 08:01 1069191                    /home/wroathe/compilers/libs/regex/libregex.so
7fe2026a8000-7fe2026ae000 rw-p 00000000 00:00 0
7fe2026ae000-7fe20284b000 r-xp 00000000 08:01 1179676                    /lib/x86_64-linux-gnu/libm-2.27.so
7fe20284b000-7fe202a4a000 ---p 0019d000 08:01 1179676                    /lib/x86_64-linux-gnu/libm-2.27.so
7fe202a4a000-7fe202a4b000 r--p 0019c000 08:01 1179676                    /lib/x86_64-linux-gnu/libm-2.27.so
7fe202a4b000-7fe202a4c000 rw-p 0019d000 08:01 1179676                    /lib/x86_64-linux-gnu/libm-2.27.so
7fe202a4c000-7fe202a60000 r-xp 00000000 08:01 1317689                    /usr/lib/x86_64-linux-gnu/libcgraph.so.6.0.0
7fe202a60000-7fe202c60000 ---p 00014000 08:01 1317689                    /usr/lib/x86_64-linux-gnu/libcgraph.so.6.0.0
7fe202c60000-7fe202c61000 r--p 00014000 08:01 1317689                    /usr/lib/x86_64-linux-gnu/libcgraph.so.6.0.0
7fe202c61000-7fe202c62000 rw-p 00015000 08:01 1317689                    /usr/lib/x86_64-linux-gnu/libcgraph.so.6.0.0
7fe202c62000-7fe202e49000 r-xp 00000000 08:01 1179672                    /lib/x86_64-linux-gnu/libc-2.27.so
7fe202e49000-7fe203049000 ---p 001e7000 08:01 1179672                    /lib/x86_64-linux-gnu/libc-2.27.so
7fe203049000-7fe20304d000 r--p 001e7000 08:01 1179672                    /lib/x86_64-linux-gnu/libc-2.27.so
7fe20304d000-7fe20304f000 rw-p 001eb000 08:01 1179672                    /lib/x86_64-linux-gnu/libc-2.27.so
7fe20304f000-7fe203053000 rw-p 00000000 00:00 0
7fe203053000-7fe20306c000 r-xp 00000000 08:01 1069242                    /home/wroathe/compilers/libs/gram/libgram.so
7fe20306c000-7fe20326c000 ---p 00019000 08:01 1069242                    /home/wroathe/compilers/libs/gram/libgram.so
7fe20326c000-7fe20326d000 r--p 00019000 08:01 1069242                    /home/wroathe/compilers/libs/gram/libgram.so
7fe20326d000-7fe20326e000 rw-p 0001a000 08:01 1069242                    /home/wroathe/compilers/libs/gram/libgram.so
7fe20326e000-7fe203272000 rw-p 00000000 00:00 0
7fe203272000-7fe203281000 r-xp 00000000 08:01 1069251                    /home/wroathe/compilers/libs/base/libbase.so
7fe203281000-7fe203480000 ---p 0000f000 08:01 1069251                    /home/wroathe/compilers/libs/base/libbase.so
7fe203480000-7fe203481000 r--p 0000e000 08:01 1069251                    /home/wroathe/compilers/libs/base/libbase.so
7fe203481000-7fe203482000 rw-p 0000f000 08:01 1069251                    /home/wroathe/compilers/libs/base/libbase.so
7fe203482000-7fe2034a9000 r-xp 00000000 08:01 1179663                    /lib/x86_64-linux-gnu/ld-2.27.so
7fe203697000-7fe20369c000 rw-p 00000000 00:00 0
7fe2036a7000-7fe2036a9000 rw-p 00000000 00:00 0
7fe2036a9000-7fe2036aa000 r--p 00027000 08:01 1179663                    /lib/x86_64-linux-gnu/ld-2.27.so
7fe2036aa000-7fe2036ab000 rw-p 00028000 08:01 1179663                    /lib/x86_64-linux-gnu/ld-2.27.so
7fe2036ab000-7fe2036ac000 rw-p 00000000 00:00 0
7ffcaae29000-7ffcaae6d000 rw-p 00000000 00:00 0                          [stack]
7ffcaae88000-7ffcaae8b000 r--p 00000000 00:00 0                          [vvar]
7ffcaae8b000-7ffcaae8d000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]

[wroathe@rohan:parser_gen] (master) $ sudo cat /proc/1320/maps
55ba838ac000-55ba838b1000 r-xp 00000000 08:01 1069186                    /home/wroathe/compilers/src/parser_gen/parser_gen
55ba83ab0000-55ba83ab1000 r--p 00004000 08:01 1069186                    /home/wroathe/compilers/src/parser_gen/parser_gen
55ba83ab1000-55ba83ab2000 rw-p 00005000 08:01 1069186                    /home/wroathe/compilers/src/parser_gen/parser_gen
55ba844bb000-55ba844dc000 rw-p 00000000 00:00 0                          [heap]
7f9e28bd3000-7f9e28bd8000 r-xp 00000000 08:01 1317687                    /usr/lib/x86_64-linux-gnu/libcdt.so.5.0.0
7f9e28bd8000-7f9e28dd8000 ---p 00005000 08:01 1317687                    /usr/lib/x86_64-linux-gnu/libcdt.so.5.0.0
7f9e28dd8000-7f9e28dd9000 r--p 00005000 08:01 1317687                    /usr/lib/x86_64-linux-gnu/libcdt.so.5.0.0
7f9e28dd9000-7f9e28dda000 rw-p 00006000 08:01 1317687                    /usr/lib/x86_64-linux-gnu/libcdt.so.5.0.0
7f9e28dda000-7f9e28de6000 r-xp 00000000 08:01 1069191                    /home/wroathe/compilers/libs/regex/libregex.so
7f9e28de6000-7f9e28fe6000 ---p 0000c000 08:01 1069191                    /home/wroathe/compilers/libs/regex/libregex.so
7f9e28fe6000-7f9e28fe7000 r--p 0000c000 08:01 1069191                    /home/wroathe/compilers/libs/regex/libregex.so
7f9e28fe7000-7f9e28fe8000 rw-p 0000d000 08:01 1069191                    /home/wroathe/compilers/libs/regex/libregex.so
7f9e28fe8000-7f9e28fee000 rw-p 00000000 00:00 0
7f9e28fee000-7f9e2918b000 r-xp 00000000 08:01 1179676                    /lib/x86_64-linux-gnu/libm-2.27.so
7f9e2918b000-7f9e2938a000 ---p 0019d000 08:01 1179676                    /lib/x86_64-linux-gnu/libm-2.27.so
7f9e2938a000-7f9e2938b000 r--p 0019c000 08:01 1179676                    /lib/x86_64-linux-gnu/libm-2.27.so
7f9e2938b000-7f9e2938c000 rw-p 0019d000 08:01 1179676                    /lib/x86_64-linux-gnu/libm-2.27.so
7f9e2938c000-7f9e293a0000 r-xp 00000000 08:01 1317689                    /usr/lib/x86_64-linux-gnu/libcgraph.so.6.0.0
7f9e293a0000-7f9e295a0000 ---p 00014000 08:01 1317689                    /usr/lib/x86_64-linux-gnu/libcgraph.so.6.0.0
7f9e295a0000-7f9e295a1000 r--p 00014000 08:01 1317689                    /usr/lib/x86_64-linux-gnu/libcgraph.so.6.0.0
7f9e295a1000-7f9e295a2000 rw-p 00015000 08:01 1317689                    /usr/lib/x86_64-linux-gnu/libcgraph.so.6.0.0
7f9e295a2000-7f9e29789000 r-xp 00000000 08:01 1179672                    /lib/x86_64-linux-gnu/libc-2.27.so
7f9e29789000-7f9e29989000 ---p 001e7000 08:01 1179672                    /lib/x86_64-linux-gnu/libc-2.27.so
7f9e29989000-7f9e2998d000 r--p 001e7000 08:01 1179672                    /lib/x86_64-linux-gnu/libc-2.27.so
7f9e2998d000-7f9e2998f000 rw-p 001eb000 08:01 1179672                    /lib/x86_64-linux-gnu/libc-2.27.so
7f9e2998f000-7f9e29993000 rw-p 00000000 00:00 0
7f9e29993000-7f9e299ac000 r-xp 00000000 08:01 1069242                    /home/wroathe/compilers/libs/gram/libgram.so
7f9e299ac000-7f9e29bac000 ---p 00019000 08:01 1069242                    /home/wroathe/compilers/libs/gram/libgram.so
7f9e29bac000-7f9e29bad000 r--p 00019000 08:01 1069242                    /home/wroathe/compilers/libs/gram/libgram.so
7f9e29bad000-7f9e29bae000 rw-p 0001a000 08:01 1069242                    /home/wroathe/compilers/libs/gram/libgram.so
7f9e29bae000-7f9e29bb2000 rw-p 00000000 00:00 0
7f9e29bb2000-7f9e29bc1000 r-xp 00000000 08:01 1069251                    /home/wroathe/compilers/libs/base/libbase.so
7f9e29bc1000-7f9e29dc0000 ---p 0000f000 08:01 1069251                    /home/wroathe/compilers/libs/base/libbase.so
7f9e29dc0000-7f9e29dc1000 r--p 0000e000 08:01 1069251                    /home/wroathe/compilers/libs/base/libbase.so
7f9e29dc1000-7f9e29dc2000 rw-p 0000f000 08:01 1069251                    /home/wroathe/compilers/libs/base/libbase.so
7f9e29dc2000-7f9e29de9000 r-xp 00000000 08:01 1179663                    /lib/x86_64-linux-gnu/ld-2.27.so
7f9e29fd7000-7f9e29fdc000 rw-p 00000000 00:00 0
7f9e29fe7000-7f9e29fe9000 rw-p 00000000 00:00 0
7f9e29fe9000-7f9e29fea000 r--p 00027000 08:01 1179663                    /lib/x86_64-linux-gnu/ld-2.27.so
7f9e29fea000-7f9e29feb000 rw-p 00028000 08:01 1179663                    /lib/x86_64-linux-gnu/ld-2.27.so
7f9e29feb000-7f9e29fec000 rw-p 00000000 00:00 0
7ffeccd6a000-7ffeccdad000 rw-p 00000000 00:00 0                          [stack]
7ffeccdf8000-7ffeccdfb000 r--p 00000000 00:00 0                          [vvar]
7ffeccdfb000-7ffeccdfd000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]
[wroathe@rohan:parser_gen] (master) $
```
