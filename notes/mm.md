```
(gdb) print *$task.mm
$4 = {
  mmap = 0xffff88807a860a90,
  mm_rb = {
    rb_node = 0xffff88807a860ab0
  },
  vmacache_seqnum = 0,
  get_unmapped_area = 0xffffffff810341d0 <arch_get_unmapped_area_topdown>,
  mmap_base = 140029348823040,
  mmap_legacy_base = 47603446345728,
  mmap_compat_base = 4160524288,
  mmap_compat_legacy_base = 1431871488,
  task_size = 140737488351232,
  highest_vm_end = 140737488351232,
  pgd = 0xffff888075864000,
  mm_users = {
    counter = 1
  },
  mm_count = {
    counter = 1
  },
  pgtables_bytes = {
    counter = 12288
  },
  map_count = 1,
  page_table_lock = {
    {
      rlock = {
        raw_lock = {
          {
            val = {
              counter = 0
            },
            {
              locked = 0 '\000',
              pending = 0 '\000'
            },
            {
              locked_pending = 0,
              tail = 0
            }
          }
        }
      }
    }
  },
  mmap_sem = {
    count = {
      counter = -4294967295
    },
    wait_list = {
      next = 0xffff88807a2752f8,
      prev = 0xffff88807a2752f8
    },
    wait_lock = {
      raw_lock = {
        {
          val = {
            counter = 0
          },
          {
            locked = 0 '\000',
            pending = 0 '\000'
          },
          {
            locked_pending = 0,
            tail = 0
          }
        }
      }
    },
    osq = {
      tail = {
        counter = 0
      }
    },
    owner = 0xffff888075a94140
  },
  mmlist = {
    next = 0xffff88807a275318,
    prev = 0xffff88807a275318
  },
  hiwater_rss = 0,
  hiwater_vm = 0,
  total_vm = 1,
  locked_vm = 0,
  pinned_vm = 0,
  data_vm = 0,
  exec_vm = 0,
  stack_vm = 1,
  def_flags = 0,
  start_code = 0,
  end_code = 0,
  start_data = 0,
  end_data = 0,
  start_brk = 0,
  brk = 0,
  start_stack = 0,
  arg_start = 140722016374031,
  arg_end = 0,
  env_start = 0,
  env_end = 0,
  saved_auxv = {0 <repeats 46 times>},
  rss_stat = {
    count = {{
        counter = 0
      }, {
        counter = 1
      }, {
        counter = 0
      }, {
        counter = 0
      }}
  },
  binfmt = 0x0 <irq_stack_union>,
  cpu_vm_mask_var = 0xffff88807a275630,
  context = {
    ctx_id = 658,
    tlb_gen = {
      counter = 0
    },
    ldt_usr_sem = {
      count = {
        counter = 0
      },
      wait_list = {
        next = 0xffff88807a275580,
        prev = 0xffff88807a275580
      },
      wait_lock = {
        raw_lock = {
          {
            val = {
              counter = 0
            },
            {
              locked = 0 '\000',
              pending = 0 '\000'
            },
            {
              locked_pending = 0,
              tail = 0
            }
          }
        }
      },
      osq = {
        tail = {
          counter = 0
        }
      },
      owner = 0x0 <irq_stack_union>
    },
    ldt = 0x0 <irq_stack_union>,
    ia32_compat = 0,
    lock = {
      owner = {
        counter = 0
      },
      wait_lock = {
        {
          rlock = {
            raw_lock = {
              {
                val = {
                  counter = 0
                },
                {
                  locked = 0 '\000',
                  pending = 0 '\000'
                },
                {
                  locked_pending = 0,
                  tail = 0
                }
              }
            }
          }
        }
      },
      osq = {
        tail = {
          counter = 0
        }
      },
      wait_list = {
        next = 0xffff88807a2755c0,
        prev = 0xffff88807a2755c0
      }
    },
    vdso = 0x0 <irq_stack_union>,
    vdso_image = 0x0 <irq_stack_union>,
    perf_rdpmc_allowed = {
      counter = 0
    },
    pkey_allocation_map = 0,
    execute_only_pkey = 0,
    bd_addr = 0xffffffffffffffff
  },
  flags = 205,
  core_state = 0x0 <irq_stack_union>,
  membarrier_state = {
    counter = 0
  },
  ioctx_lock = {
    {
      rlock = {
        raw_lock = {
          {
            val = {
              counter = 0
            },
            {
              locked = 0 '\000',
              pending = 0 '\000'
            },
            {
              locked_pending = 0,
              tail = 0
            }
          }
        }
      }
    }
  },
  ioctx_table = 0x0 <irq_stack_union>,
  owner = 0xffff888075a94140,
  user_ns = 0xffffffff82454260 <init_user_ns>,
  exe_file = 0xffff88807a27e900,
  mmu_notifier_mm = 0x0 <irq_stack_union>,
  cpumask_allocation = {
    bits = {2, 0 <repeats 127 times>}
  },
  numa_next_scan = 0,
  numa_scan_offset = 0,
  numa_scan_seq = 0,
  tlb_flush_pending = {
    counter = 0
  },
  tlb_flush_batched = false,
  uprobes_state = {
    xol_area = 0x0 <irq_stack_union>
  },
  hugetlb_usage = {
    counter = 0
  },
  async_put_work = {
    data = {
      counter = 0
    },
    entry = {
      next = 0x0 <irq_stack_union>,
      prev = 0x0 <irq_stack_union>
    },
    func = 0x0 <irq_stack_union>
  },
  hmm = 0x0 <irq_stack_union>
}
```
