```
(gdb) print *$task.mm->mmap
$6 = {
  vm_start = 140737488347136,
  vm_end = 140737488351232,
  vm_next = 0x0 <irq_stack_union>,
  vm_prev = 0x0 <irq_stack_union>,
  vm_rb = {
    __rb_parent_color = 1,
    rb_right = 0x0 <irq_stack_union>,
    rb_left = 0x0 <irq_stack_union>
  },
  rb_subtree_gap = 140737487298560,
  vm_mm = 0xffff88807a275280,
  vm_page_prot = {
    pgprot = 9223372036854775845
  },
  vm_flags = 135364979,
  shared = {
    rb = {
      __rb_parent_color = 0,
      rb_right = 0x0 <irq_stack_union>,
      rb_left = 0x0 <irq_stack_union>
    },
    rb_subtree_last = 0
  },
  anon_vma_chain = {
    next = 0xffff888075a1e9d0,
    prev = 0xffff888075a1e9d0
  },
  anon_vma = 0xffff88807c1387e8,
  vm_ops = 0x0 <irq_stack_union>,
  vm_pgoff = 34359738366,
  vm_file = 0x0 <irq_stack_union>,
  vm_prfile = 0x0 <irq_stack_union>,
  vm_private_data = 0x0 <irq_stack_union>,
  swap_readahead_info = {
    counter = 0
  },
  vm_policy = 0x0 <irq_stack_union>,
  vm_userfaultfd_ctx = {
    ctx = 0x0 <irq_stack_union>
  }
}
```
