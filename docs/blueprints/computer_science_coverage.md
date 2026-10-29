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
| 1 | File system vs DBMS: redundancy, inconsistency, sharing | T1 |
| 2 | Relation, tuple, attribute, domain — definitions | |
| 3 | Degree and cardinality [O] | |
| 4 | Candidate, primary, alternate key — identify in a table | T1 |
| 5 | Foreign key and referential integrity | T1 |
| 6 | NULL in keys; uniqueness of tuples | |
| 7 | Selection (σ) | |
| 8 | Projection (π) | |
| 9 | Union — union-compatibility | |
| 10 | Set difference | |
| 11 | Cartesian product — degree and cardinality of result [O] | T1 |
| 12 | Intersection; join as product + selection | |
| 13 | Database schema, instance, metadata, data dictionary | T1 |
| 14 | DBMS examples and uses | |
| 15 | Constraints: NOT NULL, UNIQUE, DEFAULT, PRIMARY KEY, FOREIGN KEY | T1 |
| 16 | Composite primary key | |
| 17 | Relational algebra result of combined operations [O] | |
| 18 | Database users and DBA | |
| 19 | Properties of relations (no duplicate tuples, atomic values, order irrelevant) | |
| 20 | Keys from a scenario (which column can be PK) | |

### A-SQL1 SQL I — DDL, DML, math and text functions (A 4; B1/B2 also use)
| # | Angle | Used in |
|---|---|---|
| 1 | DDL vs DML vs DQL classification | |
| 2 | CREATE TABLE with constraints | |
| 3 | ALTER TABLE — add/drop/modify column, add PK | T1 |
| 4 | DROP TABLE vs DELETE | T1 |
| 5 | INSERT INTO syntax and column list | |
| 6 | UPDATE … SET … WHERE | |
| 7 | DELETE with and without WHERE | |
| 8 | Data types: CHAR vs VARCHAR, INT, FLOAT, DATE | T1 |
| 9 | SELECT with WHERE, BETWEEN, IN, LIKE (% and _) [O] | T1 |
| 10 | DISTINCT [O] | |
| 11 | NULL handling: IS NULL / IS NOT NULL [O] | |
| 12 | POWER() [O] | |
| 13 | ROUND() with positive, zero and negative places [O] | T1 |
| 14 | MOD() [O] | |
| 15 | UPPER/LOWER/UCASE/LCASE [O] | |
| 16 | MID/SUBSTRING/SUBSTR [O] | T1 |
| 17 | LENGTH, LEFT, RIGHT [O] | |
| 18 | INSTR [O] | T1 |
| 19 | LTRIM, RTRIM, TRIM [O] | T1 |
| 20 | Nested text functions [O] | |
| 21 | Aliases (AS) and arithmetic in SELECT [O] | |
| 22 | Creating/using a database: CREATE DATABASE, USE, SHOW TABLES, DESCRIBE | |

### A-SQL2 SQL II — date, aggregates, grouping, set operations, joins (A 4; B1/B2 also use)
| # | Angle | Used in |
|---|---|---|
| 1 | NOW() and DATE() — format | |
| 2 | MONTH/MONTHNAME/YEAR/DAY/DAYNAME [O] | T1 |
| 3 | COUNT(*) vs COUNT(column) with NULLs [O] | T1 |
| 4 | SUM/AVG ignoring NULLs [O] | |
| 5 | MAX/MIN on numbers, text and dates [O] | T1 |
| 6 | COUNT(DISTINCT col) [O] | |
| 7 | GROUP BY result rows [O] | |
| 8 | HAVING vs WHERE | T1 |
| 9 | ORDER BY ASC/DESC, multiple columns [O] | |
| 10 | Order of clauses in SELECT | T1 |
| 11 | UNION / UNION ALL — duplicates [O] | |
| 12 | INTERSECT and MINUS (EXCEPT) [O] | |
| 13 | Cartesian product in SQL (FROM A, B) — row count [O] | T1 |
| 14 | Equi-join with WHERE / JOIN … ON [O] | T1 |
| 15 | NATURAL JOIN — common column appears once | |
| 16 | Aggregate functions are multi-row; single-row functions | T1 |
| 17 | Aggregates with WHERE + GROUP BY + HAVING + ORDER BY [O] | T1 |
| 18 | Table aliases in joins | |

### A-NET Computer networks (Section A 3; B1/B2 also use)
| # | Angle | Used in |
|---|---|---|
| 1 | Evolution: ARPANET, NSFNET, Internet | |
| 2 | PAN, LAN, MAN, WAN — range and examples | |
| 3 | Modem — modulation/demodulation | |
| 4 | Ethernet card (NIC), MAC address | |
| 5 | Repeater — regenerates signal | |
| 6 | Hub vs switch | T1 |
| 7 | Router vs gateway | |
| 8 | Bus topology | |
| 9 | Star topology | |
| 10 | Ring topology | |
| 11 | Mesh topology — links n(n−1)/2 [O] | T1 |
| 12 | Tree topology | |
| 13 | MAC address: 48-bit, OUI, NIC-specific | |
| 14 | IP address: IPv4 32-bit, IPv6 128-bit; valid/invalid [O] | T1 |
| 15 | Internet vs WWW | |
| 16 | DNS — domain names to IP | |
| 17 | Choosing a device/topology for a scenario | |

### B1-EXF Exception and file handling (5)
| # | Angle | Used in |
|---|---|---|
| 1 | Syntax errors vs exceptions | T1 |
| 2 | Built-in exceptions: ZeroDivisionError, ValueError, TypeError, NameError, IndexError, KeyError, IOError/FileNotFoundError, ImportError, EOFError, OverflowError, IndentationError | T1 |
| 3 | raise statement; raising with message | |
| 4 | assert statement | |
| 5 | try–except — order of except clauses [O] | |
| 6 | try–except–else [O] | T1 |
| 7 | finally always runs [O] | T1 |
| 8 | User-defined exceptions (class derived from Exception) | |
| 9 | Exception handling process: throwing, catching, call stack | |
| 10 | Text vs binary file | |
| 11 | open() modes r, w, a, r+, w+, a+, rb, wb, ab [O] | T1 |
| 12 | with statement — automatic close | |
| 13 | read(), read(n), readline(), readlines() [O] | |
| 14 | write() vs writelines(); return value of write | |
| 15 | tell() and seek(offset, whence) [O] | |
| 16 | pickle.dump / pickle.load; serialisation (pickling) | T1 |
| 17 | EOFError when reading pickle in a loop | |
| 18 | File object attributes; absolute vs relative path | |
| 19 | Counting lines/words/characters with code [O] | |
| 20 | File-handling code — find the error or missing line | |

### B1-STK Stack (4)
| # | Angle | Used in |
|---|---|---|
| 1 | LIFO; real-life examples | |
| 2 | PUSH/POP with list append/pop [O] | |
| 3 | Overflow/underflow; isEmpty, top/peek | |
| 4 | Stack contents after a sequence of operations [O] | T1 |
| 5 | Infix, prefix, postfix — definitions | T1 |
| 6 | Evaluate postfix [O] | T1 |
| 7 | Convert infix to postfix [O] | T1 |
| 8 | Operator precedence and associativity in conversion | |
| 9 | Applications: undo, browser back, function calls, bracket matching | |
| 10 | Prefix evaluation / conversion [O] | |
| 11 | Stack implementation code — identify error/missing line | |
| 12 | Balanced parentheses check with stack [O] | |

### B1-QUE Queue and deque (3)
| # | Angle | Used in |
|---|---|---|
| 1 | FIFO; front and rear; examples | T1 |
| 2 | enqueue/dequeue with list (append, pop(0)) [O] | |
| 3 | Queue contents after operations [O] | T1 |
| 4 | Underflow on dequeue from empty queue | |
| 5 | Deque — insertion/deletion at both ends | T1 |
| 6 | Deque as stack or queue | |
| 7 | Deque operations insertFront/insertRear/deletionFront/deletionRear [O] | |
| 8 | Applications: printer queue, CPU scheduling, palindrome with deque | |
| 9 | Stack vs queue comparison | |

### B1-SRCH Searching and hashing (4)
| # | Angle | Used in |
|---|---|---|
| 1 | Linear search — steps and comparisons [O] | |
| 2 | Linear search best/worst/average | T1 |
| 3 | Binary search — precondition sorted | |
| 4 | Binary search mid values / passes [O] | T1 |
| 5 | Binary search — number of comparisons, log₂n [O] | |
| 6 | Binary search best/worst case | |
| 7 | Search area halves each pass | |
| 8 | Hashing — hash function h(k) = k mod n [O] | T1 |
| 9 | Collision and collision resolution (chaining, open addressing/linear probing) [O] | |
| 10 | Perfect hash function; O(1) search | |
| 11 | Comparison: linear vs binary vs hashing | T1 |
| 12 | Searching code — identify output/error [O] | |

### B1-SORT Sorting (3)
| # | Angle | Used in |
|---|---|---|
| 1 | Bubble sort pass result [O] | T1 |
| 2 | Bubble sort comparisons/swaps count [O] | |
| 3 | Bubble sort best/worst; early exit with flag | |
| 4 | Selection sort pass result [O] | |
| 5 | Selection sort — swaps n−1; comparisons n(n−1)/2 | T1 |
| 6 | Insertion sort pass result [O] | |
| 7 | Insertion sort best case O(n) on sorted list | |
| 8 | Time complexity O(n²) of the three sorts | |
| 9 | Sorting code — identify the algorithm | |
| 10 | Stable vs number of passes; arranging steps | T1 |

### B1-DATA Understanding data (3)
| # | Angle | Used in |
|---|---|---|
| 1 | Data and its purpose; structured/unstructured | T1 |
| 2 | Data collection, storage, processing | |
| 3 | Mean [O] | |
| 4 | Median [O] | T1 |
| 5 | Mode [O] | |
| 6 | Range [O] | |
| 7 | Variance and standard deviation [O] | T1 |
| 8 | Choosing mean vs median (outliers) | |
| 9 | Measures of central tendency vs variability | |
| 10 | Data interpretation from a table [O] | |

### B1-NET Networks, DNS and data communication (4)
| # | Angle | Used in |
|---|---|---|
| 1 | Components of data communication: sender, receiver, message, medium, protocol | |
| 2 | Simplex, half-duplex, full-duplex | |
| 3 | Circuit vs packet switching | T1 |
| 4 | Twisted pair, coaxial, optical fibre — features | T1 |
| 5 | Ethernet cable | |
| 6 | Wireless: radio, microwave, infrared | |
| 7 | Bluetooth, WLAN (Wi-Fi) | |
| 8 | Mobile generations 1G–5G | |
| 9 | Protocols: HTTP, FTP, IP, PPP, SMTP/POP3 | T1 |
| 10 | Bandwidth units Hz/kHz/MHz | |
| 11 | Data transfer rate units bps–Tbps [O] | T1 |
| 12 | Channel and capacity | |
| 13 | DNS hierarchy and resolution | |
| 14 | Choosing media for a scenario | |

### B1-SEC Security aspects (3)
| # | Angle | Used in |
|---|---|---|
| 1 | Virus | T1 |
| 2 | Worm | T1 |
| 3 | Trojan horse | |
| 4 | Spam | |
| 5 | Cookies | |
| 6 | Adware, spyware, ransomware | |
| 7 | Firewall | |
| 8 | HTTP vs HTTPS | T1 |
| 9 | Hackers vs crackers (ethical hacking) | |
| 10 | Antivirus — signature/heuristic working | |
| 11 | Denial of Service / DDoS | |
| 12 | Intrusion problems | |
| 13 | Snooping and eavesdropping | |
| 14 | Prevention measures | |

### B2-SQL SQL in IP (5) — uses the A-SQL1 / A-SQL2 banks; record there.

### B2-PD1 Pandas I (8)
| # | Angle | Used in |
|---|---|---|
| 1 | Pandas, NumPy, Matplotlib — roles | |
| 2 | Series from list/array — default index [O] | |
| 3 | Series from dictionary — keys as index [O] | T1 |
| 4 | Series from scalar with index [O] | |
| 5 | Series arithmetic — alignment, NaN [O] | T1 |
| 6 | head(n) / tail(n) defaults [O] | |
| 7 | Series indexing — label vs position; slicing inclusive/exclusive [O] | T1 |
| 8 | Series attributes: index, values, size, dtype, empty, name | |
| 9 | DataFrame from dictionary of Series/lists [O] | |
| 10 | DataFrame from list of dictionaries — NaN for missing keys [O] | T1 |
| 11 | read_csv / to_csv (sep, header, index) | T1 |
| 12 | Add/delete/rename columns and rows (drop axis, rename) [O] | |
| 13 | loc vs iloc [O] | |
| 14 | Boolean indexing [O] | T1 |
| 15 | iterrows / iteritems(items) | |
| 16 | DataFrame attributes: shape, size, ndim, T, columns, index [O] | T1 |
| 17 | concat, merge, join [O] | |
| 18 | Styling/formatting (display) | |
| 19 | Series vs DataFrame; mutability of size/values | |
| 20 | Selecting a column returns a Series | |

### B2-PD2 Pandas II (6)
| # | Angle | Used in |
|---|---|---|
| 1 | describe() | |
| 2 | max/min/count/sum/mean [O] | |
| 3 | median/mode [O] | |
| 4 | quantile/quartiles [O] | T1 |
| 5 | std/var | |
| 6 | axis=0 vs axis=1 in aggregation [O] | T1 |
| 7 | groupby and aggregation [O] | |
| 8 | sort_values / sort_index [O] | |
| 9 | Deleting and renaming index (reset_index, set_index) | |
| 10 | pivot and pivot_table | T1 |
| 11 | isnull / dropna [O] | T1 |
| 12 | fillna [O] | T1 |
| 13 | read_sql / to_sql with pymysql/sqlalchemy | T1 |
| 14 | count() ignores NaN [O] | T1 |

### B2-PLT Matplotlib (6)
| # | Angle | Used in |
|---|---|---|
| 1 | Purpose of plotting; pyplot import | |
| 2 | plot() line chart; xlabel, ylabel, title | |
| 3 | bar() / barh() | |
| 4 | hist() and bins | T1 |
| 5 | pie() — autopct, labels | |
| 6 | Frequency polygon | |
| 7 | boxplot() — quartiles, outliers | |
| 8 | scatter() — correlation | T1 |
| 9 | Customising: color, linestyle (dashed, dotted), linewidth, marker | T1 |
| 10 | legend() | |
| 11 | savefig() | T1 |
| 12 | show() | |
| 13 | Pandas plot(kind=...) | T1 |
| 14 | Choosing the right chart for data | T1 |
| 15 | grid(), xticks/yticks | |

### B2-WEB Networks and the web (4)
| # | Angle | Used in |
|---|---|---|
| 1 | Network types and devices (IP view) | |
| 2 | Internet, URL structure, WWW | T1 |
| 3 | Applications: web, e-mail, chat, VoIP | T1 |
| 4 | Website vs web page | |
| 5 | Static vs dynamic web pages | T1 |
| 6 | Web server; hosting | |
| 7 | Web browsers; browser settings | |
| 8 | Add-ons and plug-ins | T1 |
| 9 | Cookies (browser view) | |
| 10 | HTML vs other languages; dynamic pages (PHP, JSP, ASP) | |

### B2-SOC Societal impacts (5)
| # | Angle | Used in |
|---|---|---|
| 1 | Digital footprint — active/passive | T1 |
| 2 | Net etiquette; communication etiquette; social media etiquette | |
| 3 | Data protection | |
| 4 | IPR — copyright, patent, trademark | T1 |
| 5 | Violation: plagiarism, copyright infringement, trademark infringement | T1 |
| 6 | Licensing: GPL, Creative Commons, Apache | |
| 7 | FOSS — examples | |
| 8 | Cybercrime — hacking, phishing, ransomware | |
| 9 | Cyberbullying, cyber trolls | |
| 10 | Indian IT Act 2000 (amended 2008) | T1 |
| 11 | Preventing cybercrime | |
| 12 | E-waste hazards | T1 |
| 13 | E-waste management — reduce, reuse, recycle | |
| 14 | Health: eye strain, ergonomics, internet addiction | |
| 15 | Identity theft | |

### B2-PBL Project-based learning (1)
| # | Angle | Used in |
|---|---|---|
| 1 | Approaches for solving projects | |
| 2 | Steps in project-based learning | |
| 3 | Teamwork and its components | T1 |
| 4 | Roles in a team; communication | |
