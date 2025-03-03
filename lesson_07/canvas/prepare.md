# Lesson 7: Operating System Features and Hardware

**Reading is key to doing well in this course. You will be required to read the provided preparation material each lesson. Take your time and read the material more than once if you don't understand it the first time.**

Section | Content
--- | ---
7.1 | [Process and Thread Scheduling](#Process-and-Thread-Scheduling)
7.2 | [Memory Management](#Memory-Management)
7.3 | [Hardware Considerations](#Hardware-Considerations)
7.4 | [File Systems](#File-Systems)

:key: = Vital concepts that we will continue to build on in coming lessons / key learning outcomes for this course.

## 7.1 Process and Thread Scheduling
Scheduling Algorithms (FIFO, Round Robin, Priority Scheduling, Multilevel Queues, etc.)
Context Switching
Preemptive vs. Non-Preemptive Multitasking

## 7.2 Memory Management
Virtual Memory
Paging and Segmentation
Memory Allocation (for Processes and Threads)

## 7.3 Hardware Considerations
Multi-core Processors (Architecture, Cache Coherence)
Hyperthreading (Simultaneous Multithreading - SMT)
NUMA (Non-Uniform Memory Access) Architectures
GPUs (Graphics Processing Units) and their Role in Parallelism (Brief Overview)
Clusters and Distributed Systems (Brief Overview)

## 7.4 File Systems
The file system plays a significant, and often overlooked, role in the performance and correctness of parallel programs.  Here's a breakdown of how the file system affects parallelism:

1. I/O Bottleneck and Parallel Performance:

Sequential Access Limitation: Traditional hard disk drives (HDDs) are inherently sequential access devices. While they can handle multiple requests concurrently, true parallelism is limited by the physical movement of the read/write head. This is a major bottleneck. If multiple threads/processes are all trying to read or write to different locations on the same HDD, performance degrades significantly due to "seek time" (the time it takes for the head to move). The OS's I/O scheduler tries to optimize this, but there are limits.
Solid State Drives (SSDs): SSDs, with their lack of moving parts, significantly mitigate this issue. They have much lower latency and can handle concurrent requests with far less performance degradation. However, even SSDs have limits on their bandwidth and the number of simultaneous operations they can efficiently handle. Different SSD technologies (SATA, NVMe) have different performance characteristics.
File System Caching: Operating systems use file system caches (often called the "buffer cache" or "page cache") to keep frequently accessed data in RAM. This dramatically speeds up reads, if the data is already in the cache. However, cache coherency becomes a concern in parallel scenarios.
Write-Back vs. Write-Through Caching:
Write-Back: Changes are written to the cache, and only periodically flushed to disk. This improves performance but introduces a risk of data loss if there's a power failure. In parallel programs, if one thread writes to the cache and another tries to read from it before the data is flushed to disk, the second thread might read stale data.
Write-Through: Changes are immediately written to both the cache and the disk. This is safer but slower.
Buffering: Even without caching, the OS and file system drivers often use buffers to group small writes together into larger, more efficient disk operations. This buffering can affect the order in which writes from different threads/processes actually reach the disk.


2. File Locking and Synchronization:

Data Races and Inconsistency: If multiple threads/processes access the same file concurrently without proper synchronization, data corruption can occur. This is a classic race condition. For example, two processes might try to append to the same log file simultaneously, resulting in interleaved (and corrupted) log entries.
File Locking Mechanisms: Operating systems provide file locking mechanisms to prevent these issues.
Advisory Locking: A cooperative locking mechanism. Processes agree to check for locks before accessing the file. This relies on all processes behaving correctly. If one process ignores the lock, it can still cause problems.
Mandatory Locking: The operating system enforces the lock. Attempts to access a locked file without acquiring the lock will result in an error or blocking. This is more robust but can be less portable.
Lock Granularity:
Whole-File Locking: Simple, but can be a significant performance bottleneck if only a small portion of the file needs to be accessed.
Byte-Range Locking: Allows locking specific regions of a file, enabling finer-grained concurrency. This is more complex to manage but can significantly improve performance in many cases.
Deadlocks: Just like with threads and processes, improper use of file locks can lead to deadlocks. For example, process A might lock file X and then try to lock file Y, while process B locks file Y and then tries to lock file X.


3. File System Metadata Operations:
Metadata Operations: Operations like creating files, deleting files, renaming files, and changing permissions involve modifying file system metadata (inodes, directory entries, etc.). These operations are typically handled by the file system kernel code and often require exclusive access to certain data structures.
Contention: If many threads/processes are concurrently creating/deleting files in the same directory, they may contend for access to the directory's metadata, creating a bottleneck. This is less of an issue with modern, journaled file systems, but it can still occur.
Directory Structure: The organization of files and directories can impact parallelism. Having many small files in a single directory can lead to more metadata contention than having files spread across multiple directories.


4. Network File Systems (NFS, SMB/CIFS):
Network Latency: When dealing with network file systems, network latency and bandwidth become major factors. Parallel operations that involve frequent access to files over a slow network will be severely limited.
Caching and Consistency: Network file systems often employ complex caching mechanisms to improve performance. Maintaining cache coherency across multiple clients accessing the same files concurrently is a challenging problem. Different protocols (NFS, SMB) have different approaches to this, with varying trade-offs between performance and consistency.
Locking over the Network: File locking becomes even more complex in a distributed environment. The locking mechanism must be implemented across the network, and network failures can introduce additional complications.


5. File System Type and Features:
Journaling: Modern file systems (like ext4, NTFS, APFS) typically use journaling. This means that changes to the file system are first written to a journal (a log) before being applied to the main file system. This improves data integrity and recovery in case of crashes, but it can also introduce some overhead.
Copy-on-Write (COW): Some file systems (like Btrfs, ZFS) use copy-on-write. When a file is modified, the changed blocks are written to a new location on disk, and then the metadata is updated to point to the new blocks. This can improve data integrity and enable features like snapshots, but it can also affect performance in some parallel workloads.
RAID: RAID configurations, which combine multiple physical disks into a single logical unit, can have a significant effect. RAID level affects parallelization.
Distributed File Systems Systems like HDFS and Ceph are designed for parallelism and distributed data storage. They handle data replication, fault tolerance, and parallel access across multiple nodes.
Practical Implications for Parallel Programming:

Minimize File I/O: If possible, design your parallel program to minimize file I/O during the computationally intensive parts. Load data into memory before starting parallel processing, and write results only when necessary.
Use SSDs: Use SSDs whenever possible, especially for temporary files and data that will be accessed frequently by multiple threads/processes.
Consider File Locking: If multiple threads/processes need to modify the same file, use appropriate file locking mechanisms to prevent data corruption. Choose the appropriate lock granularity (whole-file vs. byte-range).
Optimize Directory Structure: Avoid having too many files in a single directory, especially if those files will be created/deleted concurrently.
Network File System Awareness: Be aware of the limitations and performance characteristics of network file systems if your program will be running in a distributed environment.
Asynchronous I/O: Use asynchronous I/O operations (if available) to allow your program to continue processing while waiting for I/O operations to complete. This can improve responsiveness and overlap I/O with computation.
Memory-Mapped Files: Memory-mapped files (using mmap in POSIX systems or equivalent APIs in other OSes) can provide a way to access file data as if it were in memory, potentially simplifying parallel access and reducing the need for explicit I/O operations. However, careful synchronization is still required.
In summary, the file system isn't just a passive storage layer; it's an active participant in the execution of parallel programs. Understanding its limitations and features is crucial for achieving good performance and avoiding data corruption.
