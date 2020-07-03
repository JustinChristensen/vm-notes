```
(gdb) print $task
$2 = {
  thread_info = {
    flags = 2147483648,
    status = 0
  },
  state = 0,
  stack = 0xffffc900006f8000,
  usage = {
    counter = 2
  },
  flags = 4194304,
  ptrace = 0,
  wake_entry = {
    next = 0x0 <irq_stack_union>
  },
  on_cpu = 1,
  cpu = 1,
  wakee_flips = 3,
  wakee_flip_decay_ts = 4295013249,
  last_wakee = 0xffff88807c8a8000,
  wake_cpu = 1,
  on_rq = 1,
  prio = 120,
  static_prio = 120,
  normal_prio = 120,
  rt_priority = 0,
  sched_class = 0xffffffff81e3d080 <fair_sched_class>,
  se = {
    load = {
      weight = 1048576,
      inv_weight = 4194304
    },
    runnable_weight = 1048576,
    run_node = {
      __rb_parent_color = 1,
      rb_right = 0x0 <irq_stack_union>,
      rb_left = 0x0 <irq_stack_union>
    },
    group_node = {
      next = 0xffff88807fd22260,
      prev = 0xffff88807fd22260
    },
    on_rq = 1,
    exec_start = 483890012909,
    sum_exec_runtime = 20701165,
    vruntime = 588068003,
    prev_sum_exec_runtime = 20701165,
    nr_migrations = 0,
    statistics = {
      wait_start = 0,
      wait_max = 0,
      wait_count = 0,
      wait_sum = 0,
      iowait_count = 0,
      iowait_sum = 0,
      sleep_start = 0,
      sleep_max = 0,
      sum_sleep_runtime = 0,
      block_start = 0,
      block_max = 0,
      exec_max = 0,
      slice_max = 0,
      nr_migrations_cold = 0,
      nr_failed_migrations_affine = 0,
      nr_failed_migrations_running = 0,
      nr_failed_migrations_hot = 0,
      nr_forced_migrations = 0,
      nr_wakeups = 0,
      nr_wakeups_sync = 0,
      nr_wakeups_migrate = 0,
      nr_wakeups_local = 0,
      nr_wakeups_remote = 0,
      nr_wakeups_affine = 0,
      nr_wakeups_affine_attempts = 0,
      nr_wakeups_passive = 0,
      nr_wakeups_idle = 0
    },
    depth = 1,
    parent = 0xffff8880350c9600,
    cfs_rq = 0xffff8880350c9c00,
    my_q = 0x0 <irq_stack_union>,
    avg = {
      last_update_time = 483890012160,
      load_sum = 46278,
      runnable_load_sum = 46278,
      util_sum = 30309775,
      period_contrib = 488,
      load_avg = 1003,
      runnable_load_avg = 1003,
      util_avg = 642
    }
  },
  rt = {
    run_list = {
      next = 0xffff888075a94380,
      prev = 0xffff888075a94380
    },
    timeout = 0,
    watchdog_stamp = 0,
    time_slice = 25,
    on_rq = 0,
    on_list = 0,
    back = 0x0 <irq_stack_union>
  },
  sched_task_group = 0xffff88807c265680,
  dl = {
    rb_node = {
      __rb_parent_color = 18446612684044059576,
      rb_right = 0x0 <irq_stack_union>,
      rb_left = 0x0 <irq_stack_union>
    },
    dl_runtime = 0,
    dl_deadline = 0,
    dl_period = 0,
    dl_bw = 0,
    dl_density = 0,
    runtime = 0,
    deadline = 0,
    flags = 0,
    dl_throttled = 0,
    dl_boosted = 0,
    dl_yielded = 0,
    dl_non_contending = 0,
    dl_timer = {
      node = {
        node = {
          __rb_parent_color = 18446612684044059664,
          rb_right = 0x0 <irq_stack_union>,
          rb_left = 0x0 <irq_stack_union>
        },
        expires = 0
      },
      _softexpires = 0,
      function = 0xffffffff810d5e60 <dl_task_timer>,
      base = 0xffff88807fc1cc40,
      state = 0 '\000',
      is_rel = 0 '\000'
    },
    inactive_timer = {
      node = {
        node = {
          __rb_parent_color = 18446612684044059728,
          rb_right = 0x0 <irq_stack_union>,
          rb_left = 0x0 <irq_stack_union>
        },
        expires = 0
      },
      _softexpires = 0,
      function = 0xffffffff810d42d0 <inactive_task_timer>,
      base = 0xffff88807fc1cc40,
      state = 0 '\000',
      is_rel = 0 '\000'
    }
  },
  preempt_notifiers = {
    first = 0x0 <irq_stack_union>
  },
  btrace_seq = 0,
  policy = 0,
  nr_cpus_allowed = 2,
  cpus_allowed = {
    bits = {3, 18446744073709551615 <repeats 127 times>}
  },
  rcu_tasks_nvcsw = 0,
  rcu_tasks_holdout = 0 '\000',
  rcu_tasks_idx = 0 '\000',
  rcu_tasks_idle_cpu = -1,
  rcu_tasks_holdout_list = {
    next = 0xffff888075a948b8,
    prev = 0xffff888075a948b8
  },
  sched_info = {
    pcount = 5,
    run_delay = 3628911,
    last_arrival = 483890012909,
    last_queued = 0
  },
  tasks = {
    next = 0xffffffff82413c28 <init_task+1960>,
    prev = 0xffff88807c1b9d68
  },
  pushable_tasks = {
    prio = 140,
    prio_list = {
      next = 0xffff888075a94900,
      prev = 0xffff888075a94900
    },
    node_list = {
      next = 0xffff888075a94910,
      prev = 0xffff888075a94910
    }
  },
  pushable_dl_tasks = {
    __rb_parent_color = 18446612684044060960,
    rb_right = 0x0 <irq_stack_union>,
    rb_left = 0x0 <irq_stack_union>
  },
  mm = 0xffff88807a275280,
  active_mm = 0xffff88807a275280,
  vmacache = {
    seqnum = 0,
    vmas = {0x0 <irq_stack_union>, 0x0 <irq_stack_union>, 0x0 <irq_stack_union>, 0x0 <irq_stack_union>}
  },
  rss_stat = {
    events = 0,
    count = {0, 0, 0, 0}
  },
  exit_state = 0,
  exit_code = 0,
  exit_signal = 17,
  pdeath_signal = 0,
  jobctl = 0,
  personality = 0,
  sched_reset_on_fork = 0,
  sched_contributes_to_load = 0,
  sched_migrated = 0,
  sched_remote_wakeup = 0,
  in_execve = 1,
  in_iowait = 0,
  restore_sigmask = 0,
  memcg_may_oom = 0,
  memcg_kmem_skip_account = 0,
  no_cgroup_migration = 0,
  atomic_flags = 0,
  restart_block = {
    fn = 0xffffffff810a26e0 <do_no_restart_syscall>,
    {
      futex = {
        uaddr = 0x0 <irq_stack_union>,
        val = 0,
        flags = 0,
        bitset = 0,
        time = 0,
        uaddr2 = 0x0 <irq_stack_union>
      },
      nanosleep = {
        clockid = 0,
        type = TT_NONE,
        {
          rmtp = 0x0 <irq_stack_union>,
          compat_rmtp = 0x0 <irq_stack_union>
        },
        expires = 0
      },
      poll = {
        ufds = 0x0 <irq_stack_union>,
        nfds = 0,
        has_timeout = 0,
        tv_sec = 0,
        tv_nsec = 0
      }
    }
  },
  pid = 518,
  tgid = 518,
  stack_canary = 12003602513935962112,
  real_parent = 0xffff88807c1b95c0,
  parent = 0xffff88807c1b95c0,
  children = {
    next = 0xffff888075a94a08,
    prev = 0xffff888075a94a08
  },
  sibling = {
    next = 0xffff88807c1b9e88,
    prev = 0xffff88807c1b9e88
  },
  group_leader = 0xffff888075a94140,
  ptraced = {
    next = 0xffff888075a94a30,
    prev = 0xffff888075a94a30
  },
  ptrace_entry = {
    next = 0xffff888075a94a40,
    prev = 0xffff888075a94a40
  },
  pids = {{
      node = {
        next = 0x0 <irq_stack_union>,
        pprev = 0xffff88807aec3908
      },
      pid = 0xffff88807aec3900
    }, {
      node = {
        next = 0x0 <irq_stack_union>,
        pprev = 0xffff88807aec3910
      },
      pid = 0xffff88807aec3900
    }, {
      node = {
        next = 0xffff88807c1b9f00,
        pprev = 0xffff8880359e7e18
      },
      pid = 0xffff8880359e7e00
    }},
  thread_group = {
    next = 0xffff888075a94a98,
    prev = 0xffff888075a94a98
  },
  thread_node = {
    next = 0xffff88807aee8010,
    prev = 0xffff88807aee8010
  },
  vfork_done = 0x0 <irq_stack_union>,
  set_child_tid = 0x7f7689d8fa10,
  clear_child_tid = 0x0 <irq_stack_union>,
  utime = 0,
  stime = 20000000,
  gtime = 0,
  prev_cputime = {
    utime = 0,
    stime = 0,
    lock = {
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
  },
  nvcsw = 1,
  nivcsw = 3,
  start_time = 483862777700,
  real_start_time = 483862784700,
  min_flt = 24,
  maj_flt = 0,
  cputime_expires = {
    utime = 0,
    stime = 0,
    sum_exec_runtime = 0
  },
  cpu_timers = {{
      next = 0xffff888075a94b48,
      prev = 0xffff888075a94b48
    }, {
      next = 0xffff888075a94b58,
      prev = 0xffff888075a94b58
    }, {
      next = 0xffff888075a94b68,
      prev = 0xffff888075a94b68
    }},
  ptracer_cred = 0x0 <irq_stack_union>,
  real_cred = 0xffff8880759c7a80,
  cred = 0xffff8880759c7a80,
  comm = "parser_gen\000\000\000\000\000",
  nameidata = 0x0 <irq_stack_union>,
  sysvsem = {
    undo_list = 0x0 <irq_stack_union>
  },
  sysvshm = {
    shm_clist = {
      next = 0xffff888075a94bb0,
      prev = 0xffff888075a94bb0
    }
  },
  last_switch_count = 0,
  fs = 0xffff88807b6b9c80,
  files = 0xffff88807c898dc0,
  nsproxy = 0xffffffff8245b320 <init_nsproxy>,
  signal = 0xffff88807aee8000,
  sighand = 0xffff88807ad3d280,
  blocked = {
    sig = {0}
  },
  real_blocked = {
    sig = {0}
  },
  saved_sigmask = {
    sig = {0}
  },
  pending = {
    list = {
      next = 0xffff888075a94c08,
      prev = 0xffff888075a94c08
    },
    signal = {
      sig = {0}
    }
  },
  sas_ss_sp = 0,
  sas_ss_size = 0,
  sas_ss_flags = 2,
  task_works = 0x0 <irq_stack_union>,
  audit_context = 0x0 <irq_stack_union>,
  loginuid = {
    val = 1000
  },
  sessionid = 2,
  seccomp = {
    mode = 0,
    filter = 0x0 <irq_stack_union>
  },
  parent_exec_id = 6,
  self_exec_id = 7,
  alloc_lock = {
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
  pi_lock = {
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
  wake_q = {
    next = 0x0 <irq_stack_union>
  },
  pi_waiters = {
    rb_root = {
      rb_node = 0x0 <irq_stack_union>
    },
    rb_leftmost = 0x0 <irq_stack_union>
  },
  pi_top_task = 0x0 <irq_stack_union>,
  pi_blocked_on = 0x0 <irq_stack_union>,
  journal_info = 0x0 <irq_stack_union>,
  bio_list = 0x0 <irq_stack_union>,
  plug = 0x0 <irq_stack_union>,
  reclaim_state = 0x0 <irq_stack_union>,
  backing_dev_info = 0x0 <irq_stack_union>,
  io_context = 0x0 <irq_stack_union>,
  ptrace_message = 0,
  last_siginfo = 0x0 <irq_stack_union>,
  ioac = {
    rchar = 1116,
    wchar = 0,
    syscr = 6,
    syscw = 0,
    read_bytes = 0,
    write_bytes = 0,
    cancelled_write_bytes = 0
  },
  acct_rss_mem1 = 5390623,
  acct_vm_mem1 = 67167966,
  acct_timexpd = 20000000,
  mems_allowed = {
    bits = {1, 0 <repeats 15 times>}
  },
  mems_allowed_seq = {
    sequence = 0
  },
  cpuset_mem_spread_rotor = -1,
  cpuset_slab_spread_rotor = -1,
  cgroups = 0xffff88807b7bf400,
  cg_list = {
    next = 0xffff88807b7bf488,
    prev = 0xffff88807c1ba248
  },
  closid = 0,
  rmid = 0,
  robust_list = 0x0 <irq_stack_union>,
  compat_robust_list = 0x0 <irq_stack_union>,
  pi_state_list = {
    next = 0xffff888075a94df0,
    prev = 0xffff888075a94df0
  },
  pi_state_cache = 0x0 <irq_stack_union>,
  futex_exit_mutex = {
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
      next = 0xffff888075a94e18,
      prev = 0xffff888075a94e18
    }
  },
  futex_state = 0,
  perf_event_ctxp = {0x0 <irq_stack_union>, 0x0 <irq_stack_union>},
  perf_event_mutex = {
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
      next = 0xffff888075a94e50,
      prev = 0xffff888075a94e50
    }
  },
  perf_event_list = {
    next = 0xffff888075a94e60,
    prev = 0xffff888075a94e60
  },
  mempolicy = 0x0 <irq_stack_union>,
  il_prev = 0,
  pref_node_fork = 0,
  numa_scan_seq = 0,
  numa_scan_period = 1000,
  numa_scan_period_max = 0,
  numa_preferred_nid = -1,
  numa_migrate_retry = 0,
  node_stamp = 0,
  last_task_numa_placement = 0,
  last_sum_exec_runtime = 0,
  numa_work = {
    next = 0xffff888075a94eb0,
    func = 0x0 <irq_stack_union>
  },
  numa_entry = {
    next = 0x0 <irq_stack_union>,
    prev = 0x0 <irq_stack_union>
  },
  numa_group = 0x0 <irq_stack_union>,
  numa_faults = 0x0 <irq_stack_union>,
  total_numa_faults = 0,
  numa_faults_locality = {0, 0, 0},
  numa_pages_migrated = 0,
  tlb_ubc = {
    arch = {
      cpumask = {
        bits = {0 <repeats 128 times>}
      }
    },
    flush_required = false,
    writable = false
  },
  rcu = {
    next = 0x0 <irq_stack_union>,
    func = 0x0 <irq_stack_union>
  },
  splice_pipe = 0x0 <irq_stack_union>,
  task_frag = {
    page = 0x0 <irq_stack_union>,
    offset = 0,
    size = 0
  },
  delays = 0xffff88807b6b9880,
  nr_dirtied = 0,
  nr_dirtied_pause = 32,
  dirty_paused_when = 0,
  timer_slack_ns = 50000,
  default_timer_slack_ns = 50000,
  curr_ret_stack = -1,
  curr_ret_depth = -1,
  ret_stack = 0x0 <irq_stack_union>,
  ftrace_timestamp = 0,
  trace_overrun = {
    counter = 0
  },
  tracing_graph_pause = {
    counter = 0
  },
  trace = 0,
  trace_recursion = 0,
  memcg_in_oom = 0x0 <irq_stack_union>,
  memcg_oom_gfp_mask = 0,
  memcg_oom_order = 0,
  memcg_nr_pages_over_high = 0,
  utask = 0x0 <irq_stack_union>,
  sequential_io = 0,
  sequential_io_avg = 0,
  pagefault_disabled = 0,
  oom_reaper_list = 0x0 <irq_stack_union>,
  stack_vm_area = 0xffff888035129380,
  stack_refcount = {
    counter = 1
  },
  patch_state = -1,
  security = 0xffff88807b677d30,
  thread = {
    tls_array = {{
        limit0 = 0,
        base0 = 0,
        base1 = 0,
        type = 0,
        s = 0,
        dpl = 0,
        p = 0,
        limit1 = 0,
        avl = 0,
        l = 0,
        d = 0,
        g = 0,
        base2 = 0
      }, {
        limit0 = 0,
        base0 = 0,
        base1 = 0,
        type = 0,
        s = 0,
        dpl = 0,
        p = 0,
        limit1 = 0,
        avl = 0,
        l = 0,
        d = 0,
        g = 0,
        base2 = 0
      }, {
        limit0 = 0,
        base0 = 0,
        base1 = 0,
        type = 0,
        s = 0,
        dpl = 0,
        p = 0,
        limit1 = 0,
        avl = 0,
        l = 0,
        d = 0,
        g = 0,
        base2 = 0
      }},
    sp = 18446683600577346656,
    es = 0,
    ds = 0,
    fsindex = 0,
    gsindex = 0,
    fsbase = 140147095566144,
    gsbase = 0,
    ptrace_bps = {0x0 <irq_stack_union>, 0x0 <irq_stack_union>, 0x0 <irq_stack_union>, 0x0 <irq_stack_union>},
    debugreg6 = 0,
    ptrace_dr7 = 0,
    cr2 = 0,
    trap_nr = 0,
    error_code = 0,
    io_bitmap_ptr = 0x0 <irq_stack_union>,
    iopl = 0,
    io_bitmap_max = 0,
    addr_limit = {
      seg = 140737488351232
    },
    sig_on_uaccess_err = 0,
    uaccess_err = 0,
    fpu = {
      last_cpu = 1,
      initialized = 1 '\001',
      state = {
        fsave = {
          cwd = 895,
          swd = 0,
          twd = 0,
          fip = 0,
          fcs = 0,
          foo = 0,
          fos = 8064,
          st_space = {65535, 0 <repeats 19 times>},
          status = 0
        },
        fxsave = {
          cwd = 895,
          swd = 0,
          twd = 0,
          fop = 0,
          {
            {
              rip = 0,
              rdp = 0
            },
            {
              fip = 0,
              fcs = 0,
              foo = 0,
              fos = 0
            }
          },
          mxcsr = 8064,
          mxcsr_mask = 65535,
          st_space = {0 <repeats 32 times>},
          xmm_space = {0 <repeats 64 times>},
          padding = {0 <repeats 12 times>},
          {
            padding1 = {0 <repeats 12 times>},
            sw_reserved = {0 <repeats 12 times>}
          }
        },
        soft = {
          cwd = 895,
          swd = 0,
          twd = 0,
          fip = 0,
          fcs = 0,
          foo = 0,
          fos = 8064,
          st_space = {65535, 0 <repeats 19 times>},
          ftop = 0 '\000',
          changed = 0 '\000',
          lookahead = 0 '\000',
          no_update = 0 '\000',
          rm = 0 '\000',
          alimit = 0 '\000',
          info = 0x0 <irq_stack_union>,
          entry_eip = 0
        },
        xsave = {
          i387 = {
            cwd = 895,
            swd = 0,
            twd = 0,
            fop = 0,
            {
              {
                rip = 0,
                rdp = 0
              },
              {
                fip = 0,
                fcs = 0,
                foo = 0,
                fos = 0
              }
            },
            mxcsr = 8064,
            mxcsr_mask = 65535,
            st_space = {0 <repeats 32 times>},
            xmm_space = {0 <repeats 64 times>},
            padding = {0 <repeats 12 times>},
            {
              padding1 = {0 <repeats 12 times>},
              sw_reserved = {0 <repeats 12 times>}
            }
          },
          header = {
            xfeatures = 2147483648,
            xcomp_bv = 0,
            reserved = {1026, 18446683600576086016, 297378725211668482, 0, 0, 4294967296}
          },
          extended_state_area = 0x1600 <irq_stack_union+5632> <error: Cannot access memory at address 0x1600>
        },
        __padding = "\177\003", '\000' <repeats 22 times>, "\200\037\000\000\377\377", '\000' <repeats 485 times>...
      }
    }
  }
}
```
