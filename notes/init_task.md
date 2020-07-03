```
(gdb) print init_task
$8 = {
  thread_info = {
    flags = 2147483648,
    status = 0
  },
  state = 0,
  stack = 0xffffffff82400000 <init_thread_union>,
  usage = {
    counter = 2
  },
  flags = 2097410,
  ptrace = 0,
  wake_entry = {
    next = 0x0 <irq_stack_union>
  },
  on_cpu = 1,
  cpu = 0,
  wakee_flips = 1,
  wakee_flip_decay_ts = 4295013044,
  last_wakee = 0xffff88807c8a8000,
  wake_cpu = 0,
  on_rq = 1,
  prio = 120,
  static_prio = 120,
  normal_prio = 120,
  rt_priority = 0,
  sched_class = 0xffffffff81e3cee0 <idle_sched_class>,
  se = {
    load = {
      weight = 1048576,
      inv_weight = 4194304
    },
    runnable_weight = 0,
    run_node = {
      __rb_parent_color = 0,
      rb_right = 0x0 <irq_stack_union>,
      rb_left = 0x0 <irq_stack_union>
    },
    group_node = {
      next = 0xffffffff82413530 <init_task+176>,
      prev = 0xffffffff82413530 <init_task+176>
    },
    on_rq = 0,
    exec_start = 0,
    sum_exec_runtime = 0,
    vruntime = 0,
    prev_sum_exec_runtime = 0,
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
    depth = 0,
    parent = 0x0 <irq_stack_union>,
    cfs_rq = 0xffff88807fc218c0,
    my_q = 0x0 <irq_stack_union>,
    avg = {
      last_update_time = 0,
      load_sum = 0,
      runnable_load_sum = 0,
      util_sum = 0,
      period_contrib = 0,
      load_avg = 0,
      runnable_load_avg = 0,
      util_avg = 0
    }
  },
  rt = {
    run_list = {
      next = 0xffffffff824136c0 <init_task+576>,
      prev = 0xffffffff824136c0 <init_task+576>
    },
    timeout = 0,
    watchdog_stamp = 0,
    time_slice = 25,
    on_rq = 0,
    on_list = 0,
    back = 0x0 <irq_stack_union>
  },
  sched_task_group = 0xffffffff8295c740 <root_task_group>,
  dl = {
    rb_node = {
      __rb_parent_color = 18446744071599896312,
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
          __rb_parent_color = 18446744071599896400,
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
          __rb_parent_color = 18446744071599896464,
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
  nr_cpus_allowed = 1,
  cpus_allowed = {
    bits = {1, 18446744073709551615 <repeats 127 times>}
  },
  rcu_tasks_nvcsw = 0,
  rcu_tasks_holdout = 0 '\000',
  rcu_tasks_idx = 0 '\000',
  rcu_tasks_idle_cpu = -1,
  rcu_tasks_holdout_list = {
    next = 0xffffffff82413bf8 <init_task+1912>,
    prev = 0xffffffff82413bf8 <init_task+1912>
  },
  sched_info = {
    pcount = 0,
    run_delay = 0,
    last_arrival = 0,
    last_queued = 0
  },
  tasks = {
    next = 0xffff88807c8787a8,
    prev = 0xffff888075a948e8
  },
  pushable_tasks = {
    prio = 140,
    prio_list = {
      next = 0xffffffff82413c40 <init_task+1984>,
      prev = 0xffffffff82413c40 <init_task+1984>
    },
    node_list = {
      next = 0xffffffff82413c50 <init_task+2000>,
      prev = 0xffffffff82413c50 <init_task+2000>
    }
  },
  pushable_dl_tasks = {
    __rb_parent_color = 0,
    rb_right = 0x0 <irq_stack_union>,
    rb_left = 0x0 <irq_stack_union>
  },
  mm = 0x0 <irq_stack_union>,
  active_mm = 0xffff8880358b2100,
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
  exit_signal = 0,
  pdeath_signal = 0,
  jobctl = 0,
  personality = 0,
  sched_reset_on_fork = 0,
  sched_contributes_to_load = 0,
  sched_migrated = 0,
  sched_remote_wakeup = 0,
  in_execve = 0,
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
  pid = 0,
  tgid = 0,
  stack_canary = 17479053642727800576,
  real_parent = 0xffffffff82413480 <init_task>,
  parent = 0xffffffff82413480 <init_task>,
  children = {
    next = 0xffff88807c8788d8,
    prev = 0xffff88807c879e98
  },
  sibling = {
    next = 0xffffffff82413d58 <init_task+2264>,
    prev = 0xffffffff82413d58 <init_task+2264>
  },
  group_leader = 0xffffffff82413480 <init_task>,
  ptraced = {
    next = 0xffffffff82413d70 <init_task+2288>,
    prev = 0xffffffff82413d70 <init_task+2288>
  },
  ptrace_entry = {
    next = 0xffffffff82413d80 <init_task+2304>,
    prev = 0xffffffff82413d80 <init_task+2304>
  },
  pids = {{
      node = {
        next = 0x0 <irq_stack_union>,
        pprev = 0x0 <irq_stack_union>
      },
      pid = 0xffffffff8245b0a0 <init_struct_pid>
    }, {
      node = {
        next = 0x0 <irq_stack_union>,
        pprev = 0x0 <irq_stack_union>
      },
      pid = 0xffffffff8245b0a0 <init_struct_pid>
    }, {
      node = {
        next = 0x0 <irq_stack_union>,
        pprev = 0x0 <irq_stack_union>
      },
      pid = 0xffffffff8245b0a0 <init_struct_pid>
    }},
  thread_group = {
    next = 0xffffffff82413dd8 <init_task+2392>,
    prev = 0xffffffff82413dd8 <init_task+2392>
  },
  thread_node = {
    next = 0xffffffff82416090 <init_signals+16>,
    prev = 0xffffffff82416090 <init_signals+16>
  },
  vfork_done = 0x0 <irq_stack_union>,
  set_child_tid = 0x0 <irq_stack_union>,
  clear_child_tid = 0x0 <irq_stack_union>,
  utime = 0,
  stime = 16000000,
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
  nvcsw = 0,
  nivcsw = 3990,
  start_time = 0,
  real_start_time = 0,
  min_flt = 0,
  maj_flt = 0,
  cputime_expires = {
    utime = 0,
    stime = 0,
    sum_exec_runtime = 0
  },
  cpu_timers = {{
      next = 0xffffffff82413e88 <init_task+2568>,
      prev = 0xffffffff82413e88 <init_task+2568>
    }, {
      next = 0xffffffff82413e98 <init_task+2584>,
      prev = 0xffffffff82413e98 <init_task+2584>
    }, {
      next = 0xffffffff82413ea8 <init_task+2600>,
      prev = 0xffffffff82413ea8 <init_task+2600>
    }},
  ptracer_cred = 0x0 <irq_stack_union>,
  real_cred = 0xffffffff8245b540 <init_cred>,
  cred = 0xffffffff8245b540 <init_cred>,
  comm = "swapper/0\000\000\000\000\000\000",
  nameidata = 0x0 <irq_stack_union>,
  sysvsem = {
    undo_list = 0x0 <irq_stack_union>
  },
  sysvshm = {
    shm_clist = {
      next = 0x0 <irq_stack_union>,
      prev = 0x0 <irq_stack_union>
    }
  },
  last_switch_count = 0,
  fs = 0xffffffff825297e0 <init_fs>,
  files = 0xffffffff82523700 <init_files>,
  nsproxy = 0xffffffff8245b320 <init_nsproxy>,
  signal = 0xffffffff82416080 <init_signals>,
  sighand = 0xffffffff82415840 <init_sighand>,
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
      next = 0xffffffff82413f48 <init_task+2760>,
      prev = 0xffffffff82413f48 <init_task+2760>
    },
    signal = {
      sig = {0}
    }
  },
  sas_ss_sp = 0,
  sas_ss_size = 0,
  sas_ss_flags = 0,
  task_works = 0x0 <irq_stack_union>,
  audit_context = 0x0 <irq_stack_union>,
  loginuid = {
    val = 4294967295
  },
  sessionid = 4294967295,
  seccomp = {
    mode = 0,
    filter = 0x0 <irq_stack_union>
  },
  parent_exec_id = 0,
  self_exec_id = 0,
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
    rchar = 0,
    wchar = 0,
    syscr = 0,
    syscw = 0,
    read_bytes = 0,
    write_bytes = 0,
    cancelled_write_bytes = 0
  },
  acct_rss_mem1 = 0,
  acct_vm_mem1 = 0,
  acct_timexpd = 0,
  mems_allowed = {
    bits = {18446744073709551615 <repeats 16 times>}
  },
  mems_allowed_seq = {
    sequence = 0
  },
  cpuset_mem_spread_rotor = 0,
  cpuset_slab_spread_rotor = 0,
  cgroups = 0xffffffff824ec380 <init_css_set>,
  cg_list = {
    next = 0x0 <irq_stack_union>,
    prev = 0x0 <irq_stack_union>
  },
  closid = 0,
  rmid = 0,
  robust_list = 0x0 <irq_stack_union>,
  compat_robust_list = 0x0 <irq_stack_union>,
  pi_state_list = {
    next = 0x0 <irq_stack_union>,
    prev = 0x0 <irq_stack_union>
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
      next = 0x0 <irq_stack_union>,
      prev = 0x0 <irq_stack_union>
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
      next = 0xffffffff82414190 <init_task+3344>,
      prev = 0xffffffff82414190 <init_task+3344>
    }
  },
  perf_event_list = {
    next = 0xffffffff824141a0 <init_task+3360>,
    prev = 0xffffffff824141a0 <init_task+3360>
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
    next = 0xffffffff824141f0 <init_task+3440>,
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
  delays = 0xffff88807c86cd40,
  nr_dirtied = 0,
  nr_dirtied_pause = 0,
  dirty_paused_when = 0,
  timer_slack_ns = 50000,
  default_timer_slack_ns = 0,
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
  stack_vm_area = 0x0 <irq_stack_union>,
  stack_refcount = {
    counter = 1
  },
  patch_state = -1,
  security = 0x0 <irq_stack_union>,
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
    sp = 18446744071599832520,
    es = 0,
    ds = 0,
    fsindex = 0,
    gsindex = 0,
    fsbase = 0,
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
      seg = 18446744073709551615
    },
    sig_on_uaccess_err = 0,
    uaccess_err = 0,
    fpu = {
      last_cpu = 4294967295,
      initialized = 0 '\000',
      state = {
        fsave = {
          cwd = 0,
          swd = 0,
          twd = 0,
          fip = 0,
          fcs = 0,
          foo = 0,
          fos = 0,
          st_space = {0 <repeats 20 times>},
          status = 0
        },
        fxsave = {
          cwd = 0,
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
          mxcsr = 0,
          mxcsr_mask = 0,
          st_space = {0 <repeats 32 times>},
          xmm_space = {0 <repeats 64 times>},
          padding = {0 <repeats 12 times>},
          {
            padding1 = {0 <repeats 12 times>},
            sw_reserved = {0 <repeats 12 times>}
          }
        },
        soft = {
          cwd = 0,
          swd = 0,
          twd = 0,
          fip = 0,
          fcs = 0,
          foo = 0,
          fos = 0,
          st_space = {0 <repeats 20 times>},
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
            cwd = 0,
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
            mxcsr = 0,
            mxcsr_mask = 0,
            st_space = {0 <repeats 32 times>},
            xmm_space = {0 <repeats 64 times>},
            padding = {0 <repeats 12 times>},
            {
              padding1 = {0 <repeats 12 times>},
              sw_reserved = {0 <repeats 12 times>}
            }
          },
          header = {
            xfeatures = 0,
            xcomp_bv = 0,
            reserved = {0, 0, 0, 0, 0, 0}
          },
          extended_state_area = 0xffffffff82414a80 <init_task+5632> ""
        },
        __padding = '\000' <repeats 4095 times>
      }
    }
  }
}
```
