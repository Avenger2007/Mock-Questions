# Coverage map — CUET Computer Science / IP (308), Tests 1–15

Written **before** any test, so that repeats are prevented rather than fixed. Rules:
- A **concept angle** may be used at most **3 times** in the series, each time in a different format and with different content.
- An **output angle** (marked **[O]** — SQL result, Python output, postfix value, search/sort dry run, statistics calculation) may be reused with **new data, code or tables every time**, but at most once per section in a test.
- Pick each test's slots from these banks (least-used first) and record the test number in "Used in" (`mark_cs.py`).

## A. Case-set themes per test

| Test | B1 (Computer Science) | B2 (Informatics Practices) |
|---|---|---|
| 1 | Evaluating a postfix expression with a stack | Pandas Series created from a dictionary |
| 2 | Reading a text file — read/readline/readlines, seek/tell | DataFrame of student marks — loc, iloc, Boolean indexing |
| 3 | try–except–else–finally program trace | Line plot code — colours, styles, labels, legend |
| 4 | Queue and deque — a ticket-counter simulation | GROUP BY / HAVING on a sales table |
| 5 | Binary search dry run | DataFrame descriptive statistics |
| 6 | Bubble sort passes | Handling missing values (dropna, fillna) |
| 7 | pickle — binary file of records | Histogram and bar chart code |
| 8 | Hashing — hash function and collisions | merge / concat of DataFrames |
| 9 | Infix to postfix conversion | SQL date functions on an orders table |
| 10 | Understanding data — marks of a class | CSV import/export with Pandas |
| 11 | Insertion and selection sort comparison | E-waste and health — societal impacts |
| 12 | Network plan for a school campus | Website hosting and web browsers |
| 13 | A security incident (virus, worm, DoS, firewall) | Cybercrime and the IT Act — a scenario |
| 14 | SQL on a library database | groupby, sorting and pivot in Pandas |
| 15 | Data communication — bandwidth, data rate, switching | SQL text functions on a customer table |

## B. Angle banks

### A-DB Database concepts (Section A, 4 per test; B1 also uses this bank)
| # | Angle | Used in |
|---|---|---|
| 1 | File system vs DBMS: redundancy, inconsistency, sharing | T1, T4, T14 |
| 2 | Relation, tuple, attribute, domain — definitions | T3, T8, T12 |
| 3 | Degree and cardinality [O] | T2, T9 |
| 4 | Candidate, primary, alternate key — identify in a table | T1, T4, T7, T13 |
| 5 | Foreign key and referential integrity | T1, T4, T14 |
| 6 | NULL in keys; uniqueness of tuples | T3, T6 |
| 7 | Selection (σ) | T2, T7, T12 |
| 8 | Projection (π) | T4, T10, T13 |
| 9 | Union — union-compatibility | T2, T4, T8 |
| 10 | Set difference | T6, T11 |
| 11 | Cartesian product — degree and cardinality of result [O] | T1, T7, T11, T14 |
| 12 | Intersection; join as product + selection | T3, T8, T12 |
| 13 | Database schema, instance, metadata, data dictionary | T1, T6, T14 |
| 14 | DBMS examples and uses | T3, T10 |
| 15 | Constraints: NOT NULL, UNIQUE, DEFAULT, PRIMARY KEY, FOREIGN KEY | T1, T9 |
| 16 | Composite primary key | T2, T7, T9 |
| 17 | Relational algebra result of combined operations [O] | T3, T9, T14 |
| 18 | Database users and DBA | T2, T9 |
| 19 | Properties of relations (no duplicate tuples, atomic values, order irrelevant) | T2, T8 |
| 20 | Keys from a scenario (which column can be PK) | T3, T7 |
| 21 | Advantages of DBMS: sharing, security, integrity | T5, T10 |
| 22 | Domain of an attribute — identify from values | T5, T13 |
| 23 | Which operations need union-compatibility | T5, T10 |
| 24 | Degree and cardinality after σ and π [O] | T5, T10, T13 |
| 25 | Data inconsistency — scenario | T6 |
| 26 | NULL allowed in a foreign key | T5, T11 |
| 27 | Relational model vs file — data stored as relations | T6, T11 |
| 28 | Cartesian product followed by selection = join [O] | T7, T12 |

### A-SQL1 SQL I — DDL, DML, math and text functions (A 4; B1/B2 also use)
| # | Angle | Used in |
|---|---|---|
| 1 | DDL vs DML vs DQL classification | T2, T3, T8 |
| 2 | CREATE TABLE with constraints | T3, T6, T13 |
| 3 | ALTER TABLE — add/drop/modify column, add PK | T1, T4, T7, T9 |
| 4 | DROP TABLE vs DELETE | T1, T7, T11 |
| 5 | INSERT INTO syntax and column list | T2, T6, T8 |
| 6 | UPDATE … SET … WHERE | T2, T4, T7, T9 |
| 7 | DELETE with and without WHERE | T3, T6, T11 |
| 8 | Data types: CHAR vs VARCHAR, INT, FLOAT, DATE | T1, T2, T8, T9 |
| 9 | SELECT with WHERE, BETWEEN, IN, LIKE (% and _) [O] | T1, T2, T4, T6, T8, T11, T12, T13, T14 |
| 10 | DISTINCT [O] | T3, T7, T9, T12, T13 |
| 11 | NULL handling: IS NULL / IS NOT NULL [O] | T3, T6, T8, T10 |
| 12 | POWER() [O] | T2, T5, T6, T7, T11, T12, T14 |
| 13 | ROUND() with positive, zero and negative places [O] | T1, T4, T6, T7, T8, T10, T11, T13, T14 |
| 14 | MOD() [O] | T2, T3, T5, T6, T7, T10, T12, T14 |
| 15 | UPPER/LOWER/UCASE/LCASE [O] | T3, T7, T10, T11, T12, T13 |
| 16 | MID/SUBSTRING/SUBSTR [O] | T1, T3, T5, T6, T9, T11, T12 |
| 17 | LENGTH, LEFT, RIGHT [O] | T3, T5, T6, T7, T10, T11, T12, T13 |
| 18 | INSTR [O] | T1, T4, T5, T6, T7, T10, T11, T12, T14 |
| 19 | LTRIM, RTRIM, TRIM [O] | T1, T4, T8, T13 |
| 20 | Nested text functions [O] | T3, T5, T14 |
| 21 | Aliases (AS) and arithmetic in SELECT [O] | T3, T7 |
| 22 | Creating/using a database: CREATE DATABASE, USE, SHOW TABLES, DESCRIBE | T2, T4, T7, T9 |
| 23 | INSERT with NULL / partial column list | T5, T10 |
| 24 | UPDATE several columns at once | T5, T12 |
| 25 | Arithmetic with NULL gives NULL [O] | T5, T13, T14 |
| 26 | AND / OR / NOT in WHERE [O] | T5, T9, T12 |
| 27 | DATE literal format and comparison [O] | T6 |
| 28 | Error spotting in DDL/DML syntax | T5, T8 |
| 29 | Text functions combined with numbers (e.g. LENGTH of a value) [O] | T5, T10 |
| 30 | Comparison with BETWEEN on dates/text [O] | T6, T10, T11 |

### A-SQL2 SQL II — date, aggregates, grouping, set operations, joins (A 4; B1/B2 also use)
| # | Angle | Used in |
|---|---|---|
| 1 | NOW() and DATE() — format | T2, T10, T13 |
| 2 | MONTH/MONTHNAME/YEAR/DAY/DAYNAME [O] | T1, T2, T3, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14 |
| 3 | COUNT(*) vs COUNT(column) with NULLs [O] | T1, T7, T11, T14 |
| 4 | SUM/AVG ignoring NULLs [O] | T2, T4, T7, T8, T12, T13 |
| 5 | MAX/MIN on numbers, text and dates [O] | T1, T3, T4, T7, T8, T9, T10, T13 |
| 6 | COUNT(DISTINCT col) [O] | T2, T8, T10, T12 |
| 7 | GROUP BY result rows [O] | T3, T4, T7, T11, T12, T14 |
| 8 | HAVING vs WHERE | T1, T4, T7, T8 |
| 9 | ORDER BY ASC/DESC, multiple columns [O] | T2, T3, T4, T6, T9, T10, T12, T14 |
| 10 | Order of clauses in SELECT | T1, T8, T11 |
| 11 | UNION / UNION ALL — duplicates [O] | T2, T8, T12, T14 |
| 12 | INTERSECT and MINUS (EXCEPT) [O] | T3, T6, T9 |
| 13 | Cartesian product in SQL (FROM A, B) — row count [O] | T1, T7, T13 |
| 14 | Equi-join with WHERE / JOIN … ON [O] | T1, T4, T7, T9, T14 |
| 15 | NATURAL JOIN — common column appears once | T2, T8, T11, T14 |
| 16 | Aggregate functions are multi-row; single-row functions | T1, T2, T3, T8, T10 |
| 17 | Aggregates with WHERE + GROUP BY + HAVING + ORDER BY [O] | T1, T3, T4, T6, T8, T10, T11, T13, T14 |
| 18 | Table aliases in joins | T3, T11, T14 |
| 19 | COUNT(*) with WHERE and GROUP BY [O] | T5, T9, T11 |
| 20 | Non-aggregated column without GROUP BY — error/logic | T6, T10 |
| 21 | Aggregate on no matching rows (NULL / 0) [O] | T5, T9, T13 |
| 22 | Date functions in WHERE (e.g. YEAR(DOB)) [O] | T5, T9, T14 |
| 23 | ORDER BY on an expression or alias [O] | T5, T11, T14 |
| 24 | Set operations need the same number of columns | T5, T8, T12 |
| 25 | Equi-join with an extra condition [O] | T5, T10, T12 |
| 26 | GROUP BY on two columns [O] | T6, T10 |

### A-NET Computer networks (Section A 3; B1/B2 also use)
| # | Angle | Used in |
|---|---|---|
| 1 | Evolution: ARPANET, NSFNET, Internet | T3, T11 |
| 2 | PAN, LAN, MAN, WAN — range and examples | T3, T4 |
| 3 | Modem — modulation/demodulation | T3, T10 |
| 4 | Ethernet card (NIC), MAC address | T7, T13 |
| 5 | Repeater — regenerates signal | T5, T12 |
| 6 | Hub vs switch | T1, T9, T12 |
| 7 | Router vs gateway | T2, T9 |
| 8 | Bus topology | T5 |
| 9 | Star topology | T2, T12 |
| 10 | Ring topology | T6 |
| 11 | Mesh topology — links n(n−1)/2 [O] | T1, T8, T14 |
| 12 | Tree topology | T4, T11 |
| 13 | MAC address: 48-bit, OUI, NIC-specific | T2, T8 |
| 14 | IP address: IPv4 32-bit, IPv6 128-bit; valid/invalid [O] | T1, T9 |
| 15 | Internet vs WWW | T4, T13 |
| 16 | DNS — domain names to IP | T6, T10 |
| 17 | Choosing a device/topology for a scenario | T3, T8 |
| 18 | Switch vs router | T6, T13 |
| 19 | Wireless NIC / Wi-Fi card | T10, T14 |
| 20 | Advantages and limits of each topology | T7, T12 |
| 21 | IP address vs MAC address | T5 |
| 22 | Path of data through network devices | T11, T14 |
| 23 | Uses of networking: resource sharing, communication | T7, T12 |

### B1-EXF Exception and file handling (5)
| # | Angle | Used in |
|---|---|---|
| 1 | Syntax errors vs exceptions | T1, T10 |
| 2 | Built-in exceptions: ZeroDivisionError, ValueError, TypeError, NameError, IndexError, KeyError, IOError/FileNotFoundError, ImportError, EOFError, OverflowError, IndentationError | T1, T2, T3, T9 |
| 3 | raise statement; raising with message | T3, T9, T12 |
| 4 | assert statement | T4 |
| 5 | try–except — order of except clauses [O] | T6, T14 |
| 6 | try–except–else [O] | T1, T3, T8, T13 |
| 7 | finally always runs [O] | T1, T3, T13 |
| 8 | User-defined exceptions (class derived from Exception) | |
| 9 | Exception handling process: throwing, catching, call stack | T3, T8, T10 |
| 10 | Text vs binary file | T4, T9 |
| 11 | open() modes r, w, a, r+, w+, a+, rb, wb, ab [O] | T1, T6, T7, T11, T12 |
| 12 | with statement — automatic close | T5, T10 |
| 13 | read(), read(n), readline(), readlines() [O] | T2, T8, T11 |
| 14 | write() vs writelines(); return value of write | T4, T14 |
| 15 | tell() and seek(offset, whence) [O] | T2, T9, T12 |
| 16 | pickle.dump / pickle.load; serialisation (pickling) | T1, T4, T7, T14 |
| 17 | EOFError when reading pickle in a loop | T4, T7 |
| 18 | File object attributes; absolute vs relative path | T10 |
| 19 | Counting lines/words/characters with code [O] | T9, T10, T12 |
| 20 | File-handling code — find the error or missing line | T6, T11 |
| 21 | Generic except (catch-all) [O] | T5, T11 |
| 22 | One except clause for several exceptions (tuple) | T5, T12 |
| 23 | writelines() with a list [O] | T6 |
| 24 | seek() whence values 0/1/2 [O] | T5, T14 |
| 25 | r+ on a missing file; w+ truncation | T5, T14 |
| 26 | Counting lines with readline() in a loop [O] | T6, T13 |
| 27 | Dumping several objects with pickle; reading them back [O] | T8, T13 |
| 28 | Absolute vs relative path example | T8, T13 |

### B1-STK Stack (4)
| # | Angle | Used in |
|---|---|---|
| 1 | LIFO; real-life examples | T3, T12 |
| 2 | PUSH/POP with list append/pop [O] | T2, T8, T11 |
| 3 | Overflow/underflow; isEmpty, top/peek | T2, T8, T11 |
| 4 | Stack contents after a sequence of operations [O] | T1, T2, T4, T8, T13 |
| 5 | Infix, prefix, postfix — definitions | T1, T10, T14 |
| 6 | Evaluate postfix [O] | T1, T4, T6, T11, T13 |
| 7 | Convert infix to postfix [O] | T1, T2, T4, T8, T9, T12 |
| 8 | Operator precedence and associativity in conversion | T4, T7, T9 |
| 9 | Applications: undo, browser back, function calls, bracket matching | T2, T6, T11 |
| 10 | Prefix evaluation / conversion [O] | T3, T7, T12, T14 |
| 11 | Stack implementation code — identify error/missing line | T3, T7 |
| 12 | Balanced parentheses check with stack [O] | T3, T7, T12, T14 |
| 13 | Python list methods for a stack | T5 |
| 14 | Postfix with division and order of operands [O] | T5, T10 |
| 15 | Infix to postfix with brackets [O] | T5, T9, T13 |
| 16 | Prefix to infix | T6, T10 |
| 17 | Stack size after pushes and pops [O] | T6, T10, T14 |
| 18 | Reversing a string with a stack [O] | T5 |

### B1-QUE Queue and deque (3)
| # | Angle | Used in |
|---|---|---|
| 1 | FIFO; front and rear; examples | T1, T4, T8, T13 |
| 2 | enqueue/dequeue with list (append, pop(0)) [O] | T3, T4, T14 |
| 3 | Queue contents after operations [O] | T1, T4, T9, T13 |
| 4 | Underflow on dequeue from empty queue | T3, T4, T9, T12 |
| 5 | Deque — insertion/deletion at both ends | T1 |
| 6 | Deque as stack or queue | T2, T8 |
| 7 | Deque operations insertFront/insertRear/deletionFront/deletionRear [O] | T2, T4, T7, T10, T14 |
| 8 | Applications: printer queue, CPU scheduling, palindrome with deque | T2, T7 |
| 9 | Stack vs queue comparison | T3, T6 |
| 10 | Python list methods for a queue | T5, T11 |
| 11 | Front and rear after operations [O] | T6, T8, T12 |
| 12 | Palindrome check with a deque — trace [O] | T5, T7, T12 |
| 13 | Queue vs deque differences | T5 |
| 14 | size() / isEmpty() functions | T6, T9 |
| 15 | Peek at the front element (q[0]) | T10, T14 |
| 16 | Error spotting in deque code | |
| 17 | Fixed-size queue full condition | T11 |
| 18 | Queue length after n operations [O] | T10 |
| 19 | Simulating arrivals and service [O] | T11, T13 |

### B1-SRCH Searching and hashing (4)
| # | Angle | Used in |
|---|---|---|
| 1 | Linear search — steps and comparisons [O] | T2, T4, T9 |
| 2 | Linear search best/worst/average | T1, T3, T7 |
| 3 | Binary search — precondition sorted | T2, T4 |
| 4 | Binary search mid values / passes [O] | T1, T2, T5, T14 |
| 5 | Binary search — number of comparisons, log₂n [O] | T4, T5, T9, T12 |
| 6 | Binary search best/worst case | T3, T7 |
| 7 | Search area halves each pass | T3, T11 |
| 8 | Hashing — hash function h(k) = k mod n [O] | T1, T3, T6, T8, T9, T13, T14 |
| 9 | Collision and collision resolution (chaining, open addressing/linear probing) [O] | T2, T6, T8, T12 |
| 10 | Perfect hash function; O(1) search | T4, T8, T12 |
| 11 | Comparison: linear vs binary vs hashing | T1, T6 |
| 12 | Searching code — identify output/error [O] | T3, T7, T13 |
| 13 | Binary search on strings [O] | T6, T11 |
| 14 | Comparisons for a key at a given position (binary) [O] | T5, T7, T12 |
| 15 | Hash table after inserting keys [O] | T7, T8 |
| 16 | Linear search early stop on a sorted list | T6, T9 |
| 17 | Comparisons for an absent key (linear) [O] | T6, T11 |
| 18 | Sequence of mid indices in binary search [O] | T10 |
| 19 | Linear search: key at the last position [O] | T10, T14 |
| 20 | Fill in the blank in binary search code | T10, T13 |
| 21 | Choosing the hash table size | T11, T13 |
| 22 | Searching records (tuples) by a field [O] | T10, T14 |

### B1-SORT Sorting (3)
| # | Angle | Used in |
|---|---|---|
| 1 | Bubble sort pass result [O] | T1, T4, T6, T9, T13, T14 |
| 2 | Bubble sort comparisons/swaps count [O] | T3, T6, T12 |
| 3 | Bubble sort best/worst; early exit with flag | T2, T6 |
| 4 | Selection sort pass result [O] | T2, T4, T11 |
| 5 | Selection sort — swaps n−1; comparisons n(n−1)/2 | T1, T8, T11 |
| 6 | Insertion sort pass result [O] | T2, T8, T11, T13 |
| 7 | Insertion sort best case O(n) on sorted list | T3 |
| 8 | Time complexity O(n²) of the three sorts | T7, T9 |
| 9 | Sorting code — identify the algorithm | T3, T4 |
| 10 | Stable vs number of passes; arranging steps | T1, T8, T9 |
| 11 | Bubble sort in descending order — pass [O] | T5, T14 |
| 12 | Insertion sort — number of comparisons/shifts [O] | T5, T11, T14 |
| 13 | Selection sort on strings [O] | T7, T12 |
| 14 | Number of passes needed | T5 |
| 15 | Which sort makes fewest swaps | T7, T12 |
| 16 | Fill in the blank in sorting code (swap) | T10, T13 |
| 17 | Insertion sort in descending order [O] | T10 |
| 18 | Total comparisons of bubble sort without a flag [O] | T10 |

### B1-DATA Understanding data (3)
| # | Angle | Used in |
|---|---|---|
| 1 | Data and its purpose; structured/unstructured | T1, T6 |
| 2 | Data collection, storage, processing | T3 |
| 3 | Mean [O] | T2, T3, T10, T14 |
| 4 | Median [O] | T1, T9, T10, T13 |
| 5 | Mode [O] | T2, T4, T8, T10 |
| 6 | Range [O] | T2, T8, T10, T12 |
| 7 | Variance and standard deviation [O] | T1, T4, T6, T10, T12 |
| 8 | Choosing mean vs median (outliers) | T2, T12 |
| 9 | Measures of central tendency vs variability | T3, T9 |
| 10 | Data interpretation from a table [O] | T4, T7, T13 |
| 11 | Mean, median and mode of one data set [O] | T5, T7, T14 |
| 12 | Missing and incorrect data — cleaning | T5, T8 |
| 13 | Primary and secondary data sources | T5, T9 |
| 14 | Comparing spread of two data sets [O] | T6, T14 |
| 15 | Purpose of visualising data | T7 |
| 16 | Combined mean of two groups [O] | T11 |
| 17 | Effect of adding a constant on mean and spread | T10, T13 |
| 18 | Reading a frequency table [O] | T11 |
| 19 | From raw data to information — example | T11 |

### B1-NET Networks, DNS and data communication (4)
| # | Angle | Used in |
|---|---|---|
| 1 | Components of data communication: sender, receiver, message, medium, protocol | T3, T10 |
| 2 | Simplex, half-duplex, full-duplex | T2, T7 |
| 3 | Circuit vs packet switching | T1, T4, T13 |
| 4 | Twisted pair, coaxial, optical fibre — features | T1, T8, T9, T12 |
| 5 | Ethernet cable | T4, T10 |
| 6 | Wireless: radio, microwave, infrared | T3, T8 |
| 7 | Bluetooth, WLAN (Wi-Fi) | T4, T7, T14 |
| 8 | Mobile generations 1G–5G | T2, T8 |
| 9 | Protocols: HTTP, FTP, IP, PPP, SMTP/POP3 | T1, T2, T5, T6 |
| 10 | Bandwidth units Hz/kHz/MHz | T3, T9, T10 |
| 11 | Data transfer rate units bps–Tbps [O] | T1, T7, T8, T11, T13 |
| 12 | Channel and capacity | T4 |
| 13 | DNS hierarchy and resolution | T2, T4, T11 |
| 14 | Choosing media for a scenario | T3, T7, T11, T12 |
| 15 | Bluetooth piconet | T6, T14 |
| 16 | Satellite links | T5, T9 |
| 17 | Radio waves — features | T5, T9 |
| 18 | Time to send a file at a data rate [O] | T5, T6, T11, T13, T14 |
| 19 | TCP/IP | T6 |
| 20 | Bandwidth vs data transfer rate | T5, T10, T14 |

### B1-SEC Security aspects (3)
| # | Angle | Used in |
|---|---|---|
| 1 | Virus | T1, T8, T13 |
| 2 | Worm | T1, T8, T13 |
| 3 | Trojan horse | T4, T11 |
| 4 | Spam | T4, T12 |
| 5 | Cookies | T6, T14 |
| 6 | Adware, spyware, ransomware | T2, T8, T11 |
| 7 | Firewall | T2, T9, T13 |
| 8 | HTTP vs HTTPS | T1 |
| 9 | Hackers vs crackers (ethical hacking) | T3, T11 |
| 10 | Antivirus — signature/heuristic working | T3, T6, T12, T14 |
| 11 | Denial of Service / DDoS | T2, T7, T10, T13 |
| 12 | Intrusion problems | T7, T10 |
| 13 | Snooping and eavesdropping | T3, T9, T12 |
| 14 | Prevention measures | T3, T4, T8, T13 |
| 15 | How malware spreads | T5 |
| 16 | Heuristic (behaviour-based) detection | T6, T9 |
| 17 | HTTPS certificates and the padlock | T7, T10 |
| 18 | Strong password rules | T5, T11 |
| 19 | Botnets and zombie computers | T5 |
| 20 | Phishing (CS view) | T6, T14 |

### B2-SQL SQL in IP (5) — uses the A-SQL1 / A-SQL2 banks; record there.

### B2-PD1 Pandas I (8)
| # | Angle | Used in |
|---|---|---|
| 1 | Pandas, NumPy, Matplotlib — roles | T3, T9, T13 |
| 2 | Series from list/array — default index [O] | T3, T11 |
| 3 | Series from dictionary — keys as index [O] | T1, T6, T11, T14 |
| 4 | Series from scalar with index [O] | T2, T9 |
| 5 | Series arithmetic — alignment, NaN [O] | T1, T5, T13 |
| 6 | head(n) / tail(n) defaults [O] | T2, T4, T7, T13 |
| 7 | Series indexing — label vs position; slicing inclusive/exclusive [O] | T1, T2, T4, T6, T12 |
| 8 | Series attributes: index, values, size, dtype, empty, name | T2, T4, T6, T8, T13 |
| 9 | DataFrame from dictionary of Series/lists [O] | T4, T7, T11, T14 |
| 10 | DataFrame from list of dictionaries — NaN for missing keys [O] | T1, T7, T13 |
| 11 | read_csv / to_csv (sep, header, index) | T1, T3, T6, T10 |
| 12 | Add/delete/rename columns and rows (drop axis, rename) [O] | T3, T4, T7, T11, T14 |
| 13 | loc vs iloc [O] | T2, T4, T6, T7, T12, T14 |
| 14 | Boolean indexing [O] | T1, T2, T7, T13 |
| 15 | iterrows / iteritems(items) | T3, T6, T13 |
| 16 | DataFrame attributes: shape, size, ndim, T, columns, index [O] | T1, T4, T5, T7, T12 |
| 17 | concat, merge, join [O] | T3, T4, T8, T13 |
| 18 | Styling/formatting (display) | |
| 19 | Series vs DataFrame; mutability of size/values | T3, T9, T11 |
| 20 | Selecting a column returns a Series | T3, T6, T10 |
| 21 | Series from a NumPy array [O] | T5, T12 |
| 22 | Series arithmetic with a scalar [O] | T5, T9 |
| 23 | Deleting a column (del, pop, drop) | T5, T8, T14 |
| 24 | DataFrame from a list of lists with columns [O] | T5, T9, T14 |
| 25 | Renaming index labels | T5, T8, T14 |
| 26 | Boolean indexing with two conditions [O] | T6, T9, T12 |
| 27 | items() over columns | T5, T9 |
| 28 | name attribute of a Series | T6 |
| 29 | at / iat accessors [O] | T5, T11, T14 |
| 30 | read_csv with index_col | T5, T9 |
| 31 | head/tail of a column [O] | T11 |
| 32 | Selecting several columns df[[...]] [O] | T10, T12 |
| 33 | Values after transpose [O] | T11 |
| 34 | loc slices on rows and columns [O] | T10, T12 |

### B2-PD2 Pandas II (6)
| # | Angle | Used in |
|---|---|---|
| 1 | describe() | T2, T7, T12 |
| 2 | max/min/count/sum/mean [O] | T3, T4, T5, T11, T13 |
| 3 | median/mode [O] | T3, T5, T8, T10, T13 |
| 4 | quantile/quartiles [O] | T1, T3, T5, T12 |
| 5 | std/var | T2, T8 |
| 6 | axis=0 vs axis=1 in aggregation [O] | T1, T4, T8, T9, T12 |
| 7 | groupby and aggregation [O] | T2, T4, T7, T9, T10, T11, T13, T14 |
| 8 | sort_values / sort_index [O] | T2, T4, T9, T12, T13, T14 |
| 9 | Deleting and renaming index (reset_index, set_index) | T2, T8 |
| 10 | pivot and pivot_table | T1, T3, T9, T14 |
| 11 | isnull / dropna [O] | T1, T2, T6, T9, T12 |
| 12 | fillna [O] | T1, T4, T6, T11 |
| 13 | read_sql / to_sql with pymysql/sqlalchemy | T1, T3, T9 |
| 14 | count() ignores NaN [O] | T1, T4, T5 |
| 15 | groupby with several aggregates [O] | T7 |
| 16 | Strategies for missing data | T5, T6, T11 |
| 17 | sort_values on several columns [O] | T7, T11, T13 |
| 18 | Column-wise max/min of a DataFrame [O] | T7 |
| 19 | pivot vs pivot_table | T7, T11 |
| 20 | dropna(how=all) / thresh [O] | T6, T8, T12 |
| 21 | Statistics skip non-numeric columns | T13 |
| 22 | mode() of a DataFrame column | T10 |
| 23 | Range per column via max − min [O] | T10 |
| 24 | groupby with count [O] | T10 |
| 25 | Interpreting describe() output [O] | T10 |

### B2-PLT Matplotlib (6)
| # | Angle | Used in |
|---|---|---|
| 1 | Purpose of plotting; pyplot import | T4, T6 |
| 2 | plot() line chart; xlabel, ylabel, title | T2, T3, T13 |
| 3 | bar() / barh() | T2, T4, T7, T12 |
| 4 | hist() and bins | T1, T4, T6, T7, T9, T11 |
| 5 | pie() — autopct, labels | T2, T4, T8 |
| 6 | Frequency polygon | T3, T9, T12 |
| 7 | boxplot() — quartiles, outliers | T2, T9, T14 |
| 8 | scatter() — correlation | T1, T6, T12 |
| 9 | Customising: color, linestyle (dashed, dotted), linewidth, marker | T1, T2, T3, T12 |
| 10 | legend() | T2, T3, T10, T14 |
| 11 | savefig() | T1, T8 |
| 12 | show() | T4, T8, T11 |
| 13 | Pandas plot(kind=...) | T1, T8, T9, T13 |
| 14 | Choosing the right chart for data | T1, T6, T8, T11 |
| 15 | grid(), xticks/yticks | T4, T8, T9, T14 |
| 16 | Pandas plot kind=line | T5, T11 |
| 17 | Pandas plot kind=hist | T5, T6, T14 |
| 18 | Pandas plot kind=box | T5 |
| 19 | Two bar series side by side (width offset) | T5, T12 |
| 20 | Marker types | T5, T9, T14 |
| 21 | kind=area | T5, T10 |
| 22 | Reading information from a chart [O] | T6, T7, T11, T12, T13, T14 |
| 23 | Font size and label arguments | T10, T13 |
| 24 | Plotting a column read from CSV | T10, T13 |
| 25 | Several lines with a legend [O] | T10, T13 |
| 26 | Bar width and colour arguments | T10, T11 |

### B2-WEB Networks and the web (4)
| # | Angle | Used in |
|---|---|---|
| 1 | Network types and devices (IP view) | T3, T9, T11 |
| 2 | Internet, URL structure, WWW | T1, T2, T7, T9, T14 |
| 3 | Applications: web, e-mail, chat, VoIP | T1, T3, T7, T8 |
| 4 | Website vs web page | T2, T7, T14 |
| 5 | Static vs dynamic web pages | T1, T6, T12 |
| 6 | Web server; hosting | T2, T4, T6, T12 |
| 7 | Web browsers; browser settings | T3, T4, T6, T12 |
| 8 | Add-ons and plug-ins | T1, T7, T9 |
| 9 | Cookies (browser view) | T2, T4, T12 |
| 10 | HTML vs other languages; dynamic pages (PHP, JSP, ASP) | T3, T4, T11 |
| 11 | E-mail: To, Cc, Bcc | T5, T8, T13 |
| 12 | Domain name registration | T5, T11 |
| 13 | IP address and DNS (IP view) | T6, T8, T12 |
| 14 | Hyperlinks | T5, T9 |
| 15 | Home network devices: modem/router | T5, T8, T14 |
| 16 | Uses of cookies | T10, T13 |
| 17 | Browser history and cache | T10, T11, T13 |
| 18 | Web page, website and web server — distinguish | T10, T14 |
| 19 | Spotting a safe website (https, padlock) | T10, T13 |

### B2-SOC Societal impacts (5)
| # | Angle | Used in |
|---|---|---|
| 1 | Digital footprint — active/passive | T1, T4, T12 |
| 2 | Net etiquette; communication etiquette; social media etiquette | T2, T7, T9 |
| 3 | Data protection | T2, T3, T8 |
| 4 | IPR — copyright, patent, trademark | T1, T7, T14 |
| 5 | Violation: plagiarism, copyright infringement, trademark infringement | T1, T3 |
| 6 | Licensing: GPL, Creative Commons, Apache | T2, T4, T9 |
| 7 | FOSS — examples | T2, T7 |
| 8 | Cybercrime — hacking, phishing, ransomware | T3, T4, T13 |
| 9 | Cyberbullying, cyber trolls | T2, T6, T12, T13 |
| 10 | Indian IT Act 2000 (amended 2008) | T1, T4, T13 |
| 11 | Preventing cybercrime | T3, T7, T13 |
| 12 | E-waste hazards | T1, T4, T9, T11 |
| 13 | E-waste management — reduce, reuse, recycle | T2, T6, T11, T12 |
| 14 | Health: eye strain, ergonomics, internet addiction | T3, T6, T8, T11 |
| 15 | Identity theft | T2, T6, T8, T13 |
| 16 | Netiquette: ethical, respectful, responsible | T5, T14 |
| 17 | Social media etiquette | T6, T8 |
| 18 | Communication etiquette | T5, T7 |
| 19 | Proprietary software vs FOSS | T5, T9 |
| 20 | Cyber safety measures | T5, T8, T9 |
| 21 | Effects of e-waste on the environment | T5 |
| 22 | Managing your digital footprint | T10, T14 |
| 23 | Avoiding plagiarism by citing sources | T10, T12 |
| 24 | Privacy settings online | T12 |
| 25 | E-waste rules in India | T10, T11 |
| 26 | Copyright infringement example | T10, T14 |
| 27 | Ethical vs unethical hacking (IP view) | T10, T14 |

### B2-PBL Project-based learning (1)
| # | Angle | Used in |
|---|---|---|
| 1 | Approaches for solving projects | T10 |
| 2 | Steps in project-based learning | T2, T3, T9 |
| 3 | Teamwork and its components | T1, T11 |
| 4 | Roles in a team; communication | T4, T8 |
| 5 | Collaborative approach | T6, T12 |
| 6 | Parts of a project report | T5, T14 |
| 7 | Planning a timeline | T7, T13 |
