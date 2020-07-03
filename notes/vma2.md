```
(gdb) print *$task->mm->mmap
$4 = {
  vm_start = 94215864111104,
  vm_end = 94215864885248,
  vm_next = 0xffff88807c359b60,
  vm_prev = 0x0 <irq_stack_union>,
  vm_rb = {
    __rb_parent_color = 18446612684153920385,
    rb_right = 0x0 <irq_stack_union>,
    rb_left = 0x0 <irq_stack_union>
  },
  rb_subtree_gap = 94215864111104,
  vm_mm = 0xffff88807aa1c200,
  vm_page_prot = {
    pgprot = 37
  },
  vm_flags = 134219893,
  shared = {
    rb = {
      __rb_parent_color = 18446612684153920440,
      rb_right = 0x0 <irq_stack_union>,
      rb_left = 0x0 <irq_stack_union>
    },
    rb_subtree_last = 188
  },
  anon_vma_chain = {
    next = 0xffff88807c359968,
    prev = 0xffff88807c359968
  },
  anon_vma = 0x0 <irq_stack_union>,
  vm_ops = 0xffffffff81e5d4c0 <ext4_file_vm_ops>,
  vm_pgoff = 0,
  vm_file = 0xffff888035066e00,
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
