Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

Unreleased
----------

Added
~~~~~
- ``Period``: one half hour, keyed on its UTC start instant, with its
  settlement and EFA dates and period numbers as derived properties
  (GC-1096). Stdlib only.
- ``SettlementDay``: the settlement calendar's day (00:00 to 24:00 London),
  sharing a base with ``EFADay``: ``periods``, ``index``, ``period(n)``,
  ``max_period`` and ``period in day``.
- Elexon settlement-pair fixture for 2026-03-29, 2026-07-15, 2026-10-25 and
  2026-11-11.

Changed
~~~~~~~
- ``EFADay`` bounds come from the shared base: ``start_time`` 41.8 us to
  under 1 us. Still returns ``pd.Timestamp`` (stdlib datetime in 0.4.0).
- ``EFADay.from_start_time`` and ``from_period_start_time`` resolve through
  ``Period.containing``; the settlement-period fix-up arithmetic is gone.

Deprecated
~~~~~~~~~~
- ``EFADay.efa_sp_from_utc`` and ``utc_from_efa_sp``: use ``index`` and
  ``period(n)``.
- Naive input to ``EFADay.from_start_time`` (read as Europe/London); it will
  raise in 0.4.0.

Fixed
~~~~~

0.2.11 - 2025-06-09
~~~~~~~~~~~~~~~~~~~

Added
~~~~~

- second test on get_efa_days

Changed
~~~~~~~

Fixed
~~~~~


0.2.10 - 2024-12-05
~~~~~~~~~~~~~~~~~~


Added
~~~~~

Changed
~~~~~~~

- allow import of get_efa_days directly from efa

Fixed
~~~~~
 


0.2.9 - 2024-12-05
~~~~~~~~~~~~~~~~~~


Added
~~~~~

- funcs.get_efa_days(start_time, end_time)

Changed
~~~~~~~

Fixed
~~~~~
 
- EFADay.from_start_time should be classmethdo







0.2.8 - 2024-10-27
~~~~~~~~~~~~~~~~~~

Added
~~~~~

Changed
~~~~~~~

Fixed
~~~~~

- Use timestamp comparison in EfaDay.__eq__() to avoid pd warnings. 


0.2.7 - 2024-10-27
~~~~~~~~~~~~~~~~~~

Added
~~~~~

Changed
~~~~~~~

Fixed
~~~~~

- Use from_start_time not from_period_start_time


0.2.6 - 2024-09-20
~~~~~~~~~~~~~~~~~~

Added
~~~~~

- EFABlock dunder methods

Changed
~~~~~~~

Fixed
~~~~~

- use consistent func name from_start_time

0.2.5 - 2024-09-20
------------------

Added
~~~~~

Changed
~~~~~~~

Fixed
~~~~~

- allow import of EFABlock from efa

0.2.4 - 2024-09-20
------------------

Added
~~~~~

- EFABlock class

Changed
~~~~~~~

Fixed
~~~~~

0.2.3 - 2024-09-20
------------------

Added
~~~~~

- efablock.from_start_time

Changed
~~~~~~~

Fixed
~~~~~

0.2.2 - 2024-09-06
------------------

Added
~~~~~

- EfaDay.start_time_index

Changed
~~~~~~~

Fixed
~~~~~

- ensure helpers.sp_from_timestamp returns int for settlement period value


0.2.1 - 2024-08-20
------------------

Changed
~~~~~~~

- Implemented vectorised helpers for faster computation.

