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
| 1 | File system vs DBMS: redundancy, inconsistency, sharing | T1, T4 |
| 2 | Relation, tuple, attribute, domain — definitions | T3 |
| 3 | Degree and cardinality [O] | T2 |
| 4 | Candidate, primary, alternate key — identify in a table | T1, T4 |
| 5 | Foreign key and referential integrity | T1, T4 |
| 6 | NULL in keys; uniqueness of tuples | T3 |
| 7 | Selection (σ) | T2 |
| 8 | Projection (π) | T4 |
| 9 | Union — union-compatibility | T2, T4 |
| 10 | Set difference | |
| 11 | Cartesian product — degree and cardinality of result [O] | T1 |
| 12 | Intersection; join as product + selection | T3 |
| 13 | Database schema, instance, metadata, data dictionary | T1 |
| 14 | DBMS examples and uses | T3 |
| 15 | Constraints: NOT NULL, UNIQUE, DEFAULT, PRIMARY KEY, FOREIGN KEY | T1 |
| 16 | Composite primary key | T2 |
| 17 | Relational algebra result of combined operations [O] | T3 |
| 18 | Database users and DBA | T2 |
| 19 | Properties of relations (no duplicate tuples, atomic values, order irrelevant) | T2 |
| 20 | Keys from a scenario (which column can be PK) | T3 |

### A-SQL1 SQL I — DDL, DML, math and text functions (A 4; B1/B2 also use)
| # | Angle | Used in |
|---|---|---|
| 1 | DDL vs DML vs DQL classification | T2, T3 |
| 2 | CREATE TABLE with constraints | T3 |
| 3 | ALTER TABLE — add/drop/modify column, add PK | T1, T4 |
| 4 | DROP TABLE vs DELETE | T1 |
| 5 | INSERT INTO syntax and column list | T2 |
| 6 | UPDATE … SET … WHERE | T2, T4 |
| 7 | DELETE with and without WHERE | T3 |
| 8 | Data types: CHAR vs VARCHAR, INT, FLOAT, DATE | T1, T2 |
| 9 | SELECT with WHERE, BETWEEN, IN, LIKE (% and _) [O] | T1, T2, T4 |
| 10 | DISTINCT [O] | T3 |
| 11 | NULL handling: IS NULL / IS NOT NULL [O] | T3 |
| 12 | POWER() [O] | T2 |
| 13 | ROUND() with positive, zero and negative places [O] | T1, T4 |
| 14 | MOD() [O] | T2, T3 |
| 15 | UPPER/LOWER/UCASE/LCASE [O] | T3 |
| 16 | MID/SUBSTRING/SUBSTR [O] | T1, T3 |
| 17 | LENGTH, LEFT, RIGHT [O] | T3 |
| 18 | INSTR [O] | T1, T4 |
| 19 | LTRIM, RTRIM, TRIM [O] | T1, T4 |
| 20 | Nested text functions [O] | T3 |
| 21 | Aliases (AS) and arithmetic in SELECT [O] | T3 |
| 22 | Creating/using a database: CREATE DATABASE, USE, SHOW TABLES, DESCRIBE | T2, T4 |

### A-SQL2 SQL II — date, aggregates, grouping, set operations, joins (A 4; B1/B2 also use)
| # | Angle | Used in |
|---|---|---|
| 1 | NOW() and DATE() — format | T2 |
| 2 | MONTH/MONTHNAME/YEAR/DAY/DAYNAME [O] | T1, T2, T3 |
| 3 | COUNT(*) vs COUNT(column) with NULLs [O] | T1 |
| 4 | SUM/AVG ignoring NULLs [O] | T2, T4 |
| 5 | MAX/MIN on numbers, text and dates [O] | T1, T3, T4 |
| 6 | COUNT(DISTINCT col) [O] | T2 |
| 7 | GROUP BY result rows [O] | T3, T4 |
| 8 | HAVING vs WHERE | T1, T4 |
| 9 | ORDER BY ASC/DESC, multiple columns [O] | T2, T3, T4 |
| 10 | Order of clauses in SELECT | T1 |
| 11 | UNION / UNION ALL — duplicates [O] | T2 |
| 12 | INTERSECT and MINUS (EXCEPT) [O] | T3 |
| 13 | Cartesian product in SQL (FROM A, B) — row count [O] | T1 |
| 14 | Equi-join with WHERE / JOIN … ON [O] | T1, T4 |
| 15 | NATURAL JOIN — common column appears once | T2 |
| 16 | Aggregate functions are multi-row; single-row functions | T1, T2, T3 |
| 17 | Aggregates with WHERE + GROUP BY + HAVING + ORDER BY [O] | T1, T3, T4 |
| 18 | Table aliases in joins | T3 |

### A-NET Computer networks (Section A 3; B1/B2 also use)
| # | Angle | Used in |
|---|---|---|
| 1 | Evolution: ARPANET, NSFNET, Internet | T3 |
| 2 | PAN, LAN, MAN, WAN — range and examples | T3, T4 |
| 3 | Modem — modulation/demodulation | T3 |
| 4 | Ethernet card (NIC), MAC address | |
| 5 | Repeater — regenerates signal | |
| 6 | Hub vs switch | T1 |
| 7 | Router vs gateway | T2 |
| 8 | Bus topology | |
| 9 | Star topology | T2 |
| 10 | Ring topology | |
| 11 | Mesh topology — links n(n−1)/2 [O] | T1 |
| 12 | Tree topology | T4 |
| 13 | MAC address: 48-bit, OUI, NIC-specific | T2 |
| 14 | IP address: IPv4 32-bit, IPv6 128-bit; valid/invalid [O] | T1 |
| 15 | Internet vs WWW | T4 |
| 16 | DNS — domain names to IP | |
| 17 | Choosing a device/topology for a scenario | T3 |

### B1-EXF Exception and file handling (5)
| # | Angle | Used in |
|---|---|---|
| 1 | Syntax errors vs exceptions | T1 |
| 2 | Built-in exceptions: ZeroDivisionError, ValueError, TypeError, NameError, IndexError, KeyError, IOError/FileNotFoundError, ImportError, EOFError, OverflowError, IndentationError | T1, T2, T3 |
| 3 | raise statement; raising with message | T3 |
| 4 | assert statement | T4 |
| 5 | try–except — order of except clauses [O] | |
| 6 | try–except–else [O] | T1, T3 |
| 7 | finally always runs [O] | T1, T3 |
| 8 | User-defined exceptions (class derived from Exception) | |
| 9 | Exception handling process: throwing, catching, call stack | T3 |
| 10 | Text vs binary file | T4 |
| 11 | open() modes r, w, a, r+, w+, a+, rb, wb, ab [O] | T1 |
| 12 | with statement — automatic close | |
| 13 | read(), read(n), readline(), readlines() [O] | T2 |
| 14 | write() vs writelines(); return value of write | T4 |
| 15 | tell() and seek(offset, whence) [O] | T2 |
| 16 | pickle.dump / pickle.load; serialisation (pickling) | T1, T4 |
| 17 | EOFError when reading pickle in a loop | T4 |
| 18 | File object attributes; absolute vs relative path | |
| 19 | Counting lines/words/characters with code [O] | |
| 20 | File-handling code — find the error or missing line | |

### B1-STK Stack (4)
| # | Angle | Used in |
|---|---|---|
| 1 | LIFO; real-life examples | T3 |
| 2 | PUSH/POP with list append/pop [O] | T2 |
| 3 | Overflow/underflow; isEmpty, top/peek | T2 |
| 4 | Stack contents after a sequence of operations [O] | T1, T2, T4 |
| 5 | Infix, prefix, postfix — definitions | T1 |
| 6 | Evaluate postfix [O] | T1, T4 |
| 7 | Convert infix to postfix [O] | T1, T2, T4 |
| 8 | Operator precedence and associativity in conversion | T4 |
| 9 | Applications: undo, browser back, function calls, bracket matching | T2 |
| 10 | Prefix evaluation / conversion [O] | T3 |
| 11 | Stack implementation code — identify error/missing line | T3 |
| 12 | Balanced parentheses check with stack [O] | T3 |

### B1-QUE Queue and deque (3)
| # | Angle | Used in |
|---|---|---|
| 1 | FIFO; front and rear; examples | T1, T4 |
| 2 | enqueue/dequeue with list (append, pop(0)) [O] | T3, T4 |
| 3 | Queue contents after operations [O] | T1, T4 |
| 4 | Underflow on dequeue from empty queue | T3, T4 |
| 5 | Deque — insertion/deletion at both ends | T1 |
| 6 | Deque as stack or queue | T2 |
| 7 | Deque operations insertFront/insertRear/deletionFront/deletionRear [O] | T2, T4 |
| 8 | Applications: printer queue, CPU scheduling, palindrome with deque | T2 |
| 9 | Stack vs queue comparison | T3 |

### B1-SRCH Searching and hashing (4)
| # | Angle | Used in |
|---|---|---|
| 1 | Linear search — steps and comparisons [O] | T2, T4 |
| 2 | Linear search best/worst/average | T1, T3 |
| 3 | Binary search — precondition sorted | T2, T4 |
| 4 | Binary search mid values / passes [O] | T1, T2 |
| 5 | Binary search — number of comparisons, log₂n [O] | T4 |
| 6 | Binary search best/worst case | T3 |
| 7 | Search area halves each pass | T3 |
| 8 | Hashing — hash function h(k) = k mod n [O] | T1, T3 |
| 9 | Collision and collision resolution (chaining, open addressing/linear probing) [O] | T2 |
| 10 | Perfect hash function; O(1) search | T4 |
| 11 | Comparison: linear vs binary vs hashing | T1 |
| 12 | Searching code — identify output/error [O] | T3 |

### B1-SORT Sorting (3)
| # | Angle | Used in |
|---|---|---|
| 1 | Bubble sort pass result [O] | T1, T4 |
| 2 | Bubble sort comparisons/swaps count [O] | T3 |
| 3 | Bubble sort best/worst; early exit with flag | T2 |
| 4 | Selection sort pass result [O] | T2, T4 |
| 5 | Selection sort — swaps n−1; comparisons n(n−1)/2 | T1 |
| 6 | Insertion sort pass result [O] | T2 |
| 7 | Insertion sort best case O(n) on sorted list | T3 |
| 8 | Time complexity O(n²) of the three sorts | |
| 9 | Sorting code — identify the algorithm | T3, T4 |
| 10 | Stable vs number of passes; arranging steps | T1 |

### B1-DATA Understanding data (3)
| # | Angle | Used in |
|---|---|---|
| 1 | Data and its purpose; structured/unstructured | T1 |
| 2 | Data collection, storage, processing | T3 |
| 3 | Mean [O] | T2, T3 |
| 4 | Median [O] | T1 |
| 5 | Mode [O] | T2, T4 |
| 6 | Range [O] | T2 |
| 7 | Variance and standard deviation [O] | T1, T4 |
| 8 | Choosing mean vs median (outliers) | T2 |
| 9 | Measures of central tendency vs variability | T3 |
| 10 | Data interpretation from a table [O] | T4 |

### B1-NET Networks, DNS and data communication (4)
| # | Angle | Used in |
|---|---|---|
| 1 | Components of data communication: sender, receiver, message, medium, protocol | T3 |
| 2 | Simplex, half-duplex, full-duplex | T2 |
| 3 | Circuit vs packet switching | T1, T4 |
| 4 | Twisted pair, coaxial, optical fibre — features | T1 |
| 5 | Ethernet cable | T4 |
| 6 | Wireless: radio, microwave, infrared | T3 |
| 7 | Bluetooth, WLAN (Wi-Fi) | T4 |
| 8 | Mobile generations 1G–5G | T2 |
| 9 | Protocols: HTTP, FTP, IP, PPP, SMTP/POP3 | T1, T2 |
| 10 | Bandwidth units Hz/kHz/MHz | T3 |
| 11 | Data transfer rate units bps–Tbps [O] | T1 |
| 12 | Channel and capacity | T4 |
| 13 | DNS hierarchy and resolution | T2, T4 |
| 14 | Choosing media for a scenario | T3 |

### B1-SEC Security aspects (3)
| # | Angle | Used in |
|---|---|---|
| 1 | Virus | T1 |
| 2 | Worm | T1 |
| 3 | Trojan horse | T4 |
| 4 | Spam | T4 |
| 5 | Cookies | |
| 6 | Adware, spyware, ransomware | T2 |
| 7 | Firewall | T2 |
| 8 | HTTP vs HTTPS | T1 |
| 9 | Hackers vs crackers (ethical hacking) | T3 |
| 10 | Antivirus — signature/heuristic working | T3 |
| 11 | Denial of Service / DDoS | T2 |
| 12 | Intrusion problems | |
| 13 | Snooping and eavesdropping | T3 |
| 14 | Prevention measures | T3, T4 |

### B2-SQL SQL in IP (5) — uses the A-SQL1 / A-SQL2 banks; record there.

### B2-PD1 Pandas I (8)
| # | Angle | Used in |
|---|---|---|
| 1 | Pandas, NumPy, Matplotlib — roles | T3 |
| 2 | Series from list/array — default index [O] | T3 |
| 3 | Series from dictionary — keys as index [O] | T1 |
| 4 | Series from scalar with index [O] | T2 |
| 5 | Series arithmetic — alignment, NaN [O] | T1 |
| 6 | head(n) / tail(n) defaults [O] | T2, T4 |
| 7 | Series indexing — label vs position; slicing inclusive/exclusive [O] | T1, T2, T4 |
| 8 | Series attributes: index, values, size, dtype, empty, name | T2, T4 |
| 9 | DataFrame from dictionary of Series/lists [O] | T4 |
| 10 | DataFrame from list of dictionaries — NaN for missing keys [O] | T1 |
| 11 | read_csv / to_csv (sep, header, index) | T1, T3 |
| 12 | Add/delete/rename columns and rows (drop axis, rename) [O] | T3, T4 |
| 13 | loc vs iloc [O] | T2, T4 |
| 14 | Boolean indexing [O] | T1, T2 |
| 15 | iterrows / iteritems(items) | T3 |
| 16 | DataFrame attributes: shape, size, ndim, T, columns, index [O] | T1, T4 |
| 17 | concat, merge, join [O] | T3, T4 |
| 18 | Styling/formatting (display) | |
| 19 | Series vs DataFrame; mutability of size/values | T3 |
| 20 | Selecting a column returns a Series | T3 |

### B2-PD2 Pandas II (6)
| # | Angle | Used in |
|---|---|---|
| 1 | describe() | T2 |
| 2 | max/min/count/sum/mean [O] | T3, T4 |
| 3 | median/mode [O] | T3 |
| 4 | quantile/quartiles [O] | T1, T3 |
| 5 | std/var | T2 |
| 6 | axis=0 vs axis=1 in aggregation [O] | T1, T4 |
| 7 | groupby and aggregation [O] | T2, T4 |
| 8 | sort_values / sort_index [O] | T2, T4 |
| 9 | Deleting and renaming index (reset_index, set_index) | T2 |
| 10 | pivot and pivot_table | T1, T3 |
| 11 | isnull / dropna [O] | T1, T2 |
| 12 | fillna [O] | T1, T4 |
| 13 | read_sql / to_sql with pymysql/sqlalchemy | T1, T3 |
| 14 | count() ignores NaN [O] | T1, T4 |

### B2-PLT Matplotlib (6)
| # | Angle | Used in |
|---|---|---|
| 1 | Purpose of plotting; pyplot import | T4 |
| 2 | plot() line chart; xlabel, ylabel, title | T2, T3 |
| 3 | bar() / barh() | T2, T4 |
| 4 | hist() and bins | T1, T4 |
| 5 | pie() — autopct, labels | T2, T4 |
| 6 | Frequency polygon | T3 |
| 7 | boxplot() — quartiles, outliers | T2 |
| 8 | scatter() — correlation | T1 |
| 9 | Customising: color, linestyle (dashed, dotted), linewidth, marker | T1, T2, T3 |
| 10 | legend() | T2, T3 |
| 11 | savefig() | T1 |
| 12 | show() | T4 |
| 13 | Pandas plot(kind=...) | T1 |
| 14 | Choosing the right chart for data | T1 |
| 15 | grid(), xticks/yticks | T4 |

### B2-WEB Networks and the web (4)
| # | Angle | Used in |
|---|---|---|
| 1 | Network types and devices (IP view) | T3 |
| 2 | Internet, URL structure, WWW | T1, T2 |
| 3 | Applications: web, e-mail, chat, VoIP | T1, T3 |
| 4 | Website vs web page | T2 |
| 5 | Static vs dynamic web pages | T1 |
| 6 | Web server; hosting | T2, T4 |
| 7 | Web browsers; browser settings | T3, T4 |
| 8 | Add-ons and plug-ins | T1 |
| 9 | Cookies (browser view) | T2, T4 |
| 10 | HTML vs other languages; dynamic pages (PHP, JSP, ASP) | T3, T4 |

### B2-SOC Societal impacts (5)
| # | Angle | Used in |
|---|---|---|
| 1 | Digital footprint — active/passive | T1, T4 |
| 2 | Net etiquette; communication etiquette; social media etiquette | T2 |
| 3 | Data protection | T2, T3 |
| 4 | IPR — copyright, patent, trademark | T1 |
| 5 | Violation: plagiarism, copyright infringement, trademark infringement | T1, T3 |
| 6 | Licensing: GPL, Creative Commons, Apache | T2, T4 |
| 7 | FOSS — examples | T2 |
| 8 | Cybercrime — hacking, phishing, ransomware | T3, T4 |
| 9 | Cyberbullying, cyber trolls | T2 |
| 10 | Indian IT Act 2000 (amended 2008) | T1, T4 |
| 11 | Preventing cybercrime | T3 |
| 12 | E-waste hazards | T1, T4 |
| 13 | E-waste management — reduce, reuse, recycle | T2 |
| 14 | Health: eye strain, ergonomics, internet addiction | T3 |
| 15 | Identity theft | T2 |

### B2-PBL Project-based learning (1)
| # | Angle | Used in |
|---|---|---|
| 1 | Approaches for solving projects | |
| 2 | Steps in project-based learning | T2, T3 |
| 3 | Teamwork and its components | T1 |
| 4 | Roles in a team; communication | T4 |
