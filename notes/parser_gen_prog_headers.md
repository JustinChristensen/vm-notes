```
[wroathe@rohan:parser_gen] (master) $ readelf -lW parser_gen

Elf file type is DYN (Shared object file)
Entry point 0x17e0
There are 9 program headers, starting at offset 64

Program Headers:
  Type           Offset   VirtAddr           PhysAddr           FileSiz  MemSiz   Flg Align
  PHDR           0x000040 0x0000000000000040 0x0000000000000040 0x0001f8 0x0001f8 R   0x8
  INTERP         0x000238 0x0000000000000238 0x0000000000000238 0x00001c 0x00001c R   0x1
      [Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]
  LOAD           0x000000 0x0000000000000000 0x0000000000000000 0x004018 0x004018 R E 0x200000
  LOAD           0x004b90 0x0000000000204b90 0x0000000000204b90 0x000480 0x0004c0 RW  0x200000
  DYNAMIC        0x004be0 0x0000000000204be0 0x0000000000204be0 0x000210 0x000210 RW  0x8
  NOTE           0x000254 0x0000000000000254 0x0000000000000254 0x000044 0x000044 R   0x4
  GNU_EH_FRAME   0x003a9c 0x0000000000003a9c 0x0000000000003a9c 0x000114 0x000114 R   0x4
  GNU_STACK      0x000000 0x0000000000000000 0x0000000000000000 0x000000 0x000000 RW  0x10
  GNU_RELRO      0x004b90 0x0000000000204b90 0x0000000000204b90 0x000470 0x000470 R   0x1

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

struct loadcmd *c = &loadcmds[nloadcmds++];
c->mapstart = ALIGN_DOWN (ph->p_vaddr, GLRO(dl_pagesize));
c->mapend = ALIGN_UP (ph->p_vaddr + ph->p_filesz, GLRO(dl_pagesize));
c->dataend = ph->p_vaddr + ph->p_filesz;
c->allocend = ph->p_vaddr + ph->p_memsz;
c->mapoff = ALIGN_DOWN (ph->p_offset, GLRO(dl_pagesize));
```
