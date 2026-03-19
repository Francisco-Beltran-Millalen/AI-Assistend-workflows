# Run All Tests Skill

Run the full test suite for the Bevy graybox prototype.

## Process

1. Confirm `graybox-prototype/Cargo.toml` exists — if not, the scaffold hasn't been set up yet; tell the user.

2. Run:
   ```bash
   cd graybox-prototype && cargo test
   ```

3. Report:
   - How many tests passed / failed / skipped
   - If any failed: show the failure names and error messages
   - If all passed: confirm clearly
