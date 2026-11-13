# Changelog

Release versions follow gc-api ADR-004 "Release Versions": on 0.x a break
bumps the minor, an addition or fix bumps the patch. For this library a break
is a public name removed or renamed, a return type changed, or the Python
floor raised. Each heading is a release, tagged `vX.Y.Z`. The rule applies
from 0.4.0; 0.3.0 bumped the minor for an additive release.

## 0.3.0 - 2026-11-13

GC-1096. Additive: nothing removed, no return type changed. iris-pg stays
pinned on 0.2.20 (GC-1090).

### Added

- `Period`: one half hour, keyed on its UTC start instant, with its
  settlement and EFA dates and period numbers as derived properties. Stdlib
  only.
- `SettlementDay`: the settlement calendar's day (00:00 to 24:00 London),
  sharing a base with `EFADay`: `periods`, `index`, `period(n)`,
  `max_period` and `period in day`.
- Elexon settlement-pair fixture for 2026-03-29, 2026-07-15, 2026-10-25 and
  2026-11-11.

### Changed

- `EFADay` bounds come from the shared base: `start_time` 41.8 us to under
  1 us. Still returns `pd.Timestamp` (stdlib datetime in 0.4.0, GC-1117).
- `EFADay.from_start_time` and `from_period_start_time` resolve through
  `Period.containing`; the settlement-period fix-up arithmetic is gone.

### Deprecated

- `EFADay.efa_sp_from_utc` and `utc_from_efa_sp`: use `efa_day.index(...)`
  and `efa_day.period(n)`.
- Naive input to `EFADay.from_start_time` (read as Europe/London); it will
  raise in 0.4.0.

## 0.2.20 - 2026-10-24

### Fixed

- `EFADay.from_start_time` put the clocks-back day's last two half hours on
  the next EFA day. (GC-499, GC-871)

## 0.2.19 - 2026-03-31

### Fixed

- `EFADay.month_end`.

## 0.2.18 - 2026-03-31

### Changed

- `make_hh_options` values are zero-padded strings.

## 0.2.17 - 2026-03-31

### Added

- `EFADay.efa_sp_from_utc` and `utc_from_efa_sp`.

### Changed

- `make_hh_options` values are `efa_sp`.
- Type hints added and corrected.

## 0.2.16 - 2026-03-30

### Added

- `EFADay.make_hh_options`.

## 0.2.15 - 2026-03-15

### Added

- `EFADay.month_start` and `month_end`.

## 0.2.14 - 2026-03-15

### Added

- `EFADay.year`, `month`, `day`, `year_start` and `year_end`.

## 0.2.13 - 2025-11-07

### Added

- `EFADay.start_time_from_utc_str`.
- `tz` argument to `start_time_index`.

## 0.2.12 - 2025-10-07

### Changed

- `EFADay()` with no date gives the current EFA day.
- `start_time_index` returns a proper `Index` named `start_time`.

## 0.2.11 - 2025-06-09

### Added

- Second test on `get_efa_days`.

## 0.2.10 - 2024-12-05

### Changed

- `get_efa_days` importable directly from `efa`.

## 0.2.9 - 2024-12-05

### Added

- `funcs.get_efa_days(start_time, end_time)`.

### Fixed

- `EFADay.from_start_time` is a classmethod.

## 0.2.8 - 2024-10-27

### Fixed

- Timestamp comparison in `EFADay.__eq__` to avoid pandas warnings.

## 0.2.7 - 2024-10-27

### Fixed

- Use `from_start_time`, not `from_period_start_time`.

## 0.2.6 - 2024-09-20

### Added

- `EFABlock` dunder methods.

### Fixed

- Consistent function name `from_start_time`.

## 0.2.5 - 2024-09-20

### Fixed

- `EFABlock` importable from `efa`.

## 0.2.4 - 2024-09-20

### Added

- `EFABlock` class.

## 0.2.3 - 2024-09-20

### Added

- `efablock.from_start_time`.

## 0.2.2 - 2024-09-06

### Added

- `EFADay.start_time_index`.

### Fixed

- `helpers.sp_from_timestamp` returns an int settlement period.

## 0.2.1 - 2024-08-20

### Changed

- Vectorised helpers for faster computation.
