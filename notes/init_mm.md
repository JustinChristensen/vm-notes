```
(gdb) print init_mm
$10 = {
  mmap = 0x0 <irq_stack_union>,
  mm_rb = {
    rb_node = 0x0 <irq_stack_union>
  },
  vmacache_seqnum = 0,
  get_unmapped_area = 0x0 <irq_stack_union>,
  mmap_base = 0,
  mmap_legacy_base = 0,
  mmap_compat_base = 0,
  mmap_compat_legacy_base = 0,
  task_size = 0,
  highest_vm_end = 0,
  pgd = 0xffffffff8240a000,
  mm_users = {
    counter = 2
  },
  mm_count = {
    counter = 2
  },
  pgtables_bytes = {
    counter = 16384
  },
  map_count = 0,
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
      counter = 0
    },
    wait_list = {
      next = 0xffffffff82507d78 <init_mm+120>,
      prev = 0xffffffff82507d78 <init_mm+120>
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
  mmlist = {
    next = 0xffffffff82507d98 <init_mm+152>,
    prev = 0xffffffff82507d98 <init_mm+152>
  },
  hiwater_rss = 0,
  hiwater_vm = 0,
  total_vm = 0,
  locked_vm = 0,
  pinned_vm = 0,
  data_vm = 0,
  exec_vm = 0,
  stack_vm = 0,
  def_flags = 0,
  start_code = 18446744071578845184,
  end_code = 18446744071591440849,
  start_data = 0,
  end_data = 18446744071602357952,
  start_brk = 0,
  brk = 18446744071607762944,
  start_stack = 0,
  arg_start = 0,
  arg_end = 0,
  env_start = 0,
  env_end = 0,
  saved_auxv = {0 <repeats 46 times>},
  rss_stat = {
    count = {{
        counter = 0
      }, {
        counter = 0
      }, {
        counter = 0
      }, {
        counter = 0
      }}
  },
  binfmt = 0x0 <irq_stack_union>,
  cpu_vm_mask_var = 0xffffffff825080b0 <init_mm+944>,
  context = {
    ctx_id = 1,
    tlb_gen = {
      counter = 0
    },
    ldt_usr_sem = {
      count = {
        counter = 0
      },
      wait_list = {
        next = 0x0 <irq_stack_union>,
        prev = 0x0 <irq_stack_union>
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
        next = 0x0 <irq_stack_union>,
        prev = 0x0 <irq_stack_union>
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
  flags = 0,
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
  owner = 0x0 <irq_stack_union>,
  user_ns = 0xffffffff82454260 <init_user_ns>,
  exe_file = 0x0 <irq_stack_union>,
  mmu_notifier_mm = 0x0 <irq_stack_union>,
  cpumask_allocation = {
    bits = {0 <repeats 128 times>}
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
