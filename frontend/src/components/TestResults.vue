<template>
  <b-container>
    <div
      id="term-window"
      @mousedown="startTrackingMouse"
      @mouseup="handleTerminalClick"
    >
      <p>
        <span id="term-loc">pikachu@pokedex:~/cs329-idb&nbsp;&nbsp;</span
        ><span id="term-branch">(master)</span>
        <br />
        <span class="term-prompt"
          >&#9656;&nbsp;<input
            class="term-entry"
            ref="main_input"
            name="no_search"
            autocomplete="off"
            :value="main_prompt_text"
            v-on:input="updateInputMain"
            @keydown.enter="hitEnterMain"
        /></span>
      </p>
      <pre
        v-show="!hide_results"
        v-for="(line, index) in results"
        :key="index"
        class="term-text"
        >{{ line }}</pre
      >
      <p v-show="is_error">
        <span id="term-error">Error: Network Error</span>
      </p>
      <p v-show="can_clear">
        <span class="term-prompt"
          >&#9656;&nbsp;<input
            class="term-entry"
            ref="clear_input"
            autocomplete="off"
            :value="clear_prompt_text"
            v-on:input="updateInputClear"
            @keydown.enter="hitEnterClear"
        /></span>
      </p>
    </div>
  </b-container>
</template>

<script>
import { getTestResults } from "@/api";

const clear_target = "clear";
const main_target = "make coverage";
const result_pattern = /Ran [0-9]+ tests in ([0-9]+\.{0,1}[0-9]+)s/;
const drag_duration = 150; // milliseconds

const calcUpdatedText = function(current, target, event_type) {
  if (event_type == "deleteContentBackward") {
    if (current.length <= 1) return "";

    return current.slice(0, current.length - 1);
  } else if (event_type == "insertText") {
    if (current.length == target.length) return target;

    return target.slice(0, current.length + 1);
  } else {
    return current;
  }
};

// Provides a delay in milliseconds for emulating testing time.
// Finds the line from the test results describing how long they took.
// Extracts the time (in seconds) using RegEx and converts to millimeters.
// If the RegEx fails, it defaults to 3000.
const calcDuration = function(results) {
  for (const index in results) {
    const row = results[index];
    const matches = row.match(result_pattern);
    if (matches && matches.length > 1) {
      try {
        return 1000 * Number.parseFloat(matches[1]);
      } catch (error) {
        // RegEx grabbed a match that wasn't a numeric-literal.
        // The RegEx pattern is probably bad, no point in further iteration.
        break;
      }
    }
  }
  return 3000; // Just in case the RegEx fails.
};

export default {
  name: "TestResults",
  data() {
    return {
      main_prompt_text: "",
      clear_prompt_text: "",
      results: [],
      can_clear: false,
      hide_results: false,
      is_error: false,
      last_mouse_event: -1
    };
  },
  methods: {
    advancePrompt: function() {
      // Reveals the "clear" prompt and places it in focus.
      this.can_clear = true;
      this.$nextTick(() => {
        this.$refs.clear_input.focus();
      });
    },
    showTestResultsCached: function(target_duration, elapsed = 0, max = 7000) {
      // Cached requests don't re-run tests, and return almost instantly.
      // Use a delay to make testing feel realistic for cached requests.
      // Limit the duration to 7 seconds (trades realism for usability).
      const duration = Math.min(Math.max(0, target_duration - elapsed), max);
      const self = this;
      const handler = function() {
        // Reveal the results and move to the next terminal prompt.
        self.hide_results = false;
        self.advancePrompt();
      };

      // The delay will always be ignored when (duration <= 0).
      if (duration > 0) {
        setTimeout(handler, duration);
      } else {
        handler();
      }
    },
    hitEnterMain: function() {
      // Do nothing unless the full command is written.
      if (this.main_prompt_text != main_target) return;

      this.$refs.main_input.blur(); // Release the focus on the main prompt.

      if (this.results.length > 0) {
        // The data is already saved locally. Just simulate the delay.
        const duration = calcDuration(this.results);
        this.showTestResultsCached(duration);
      } else {
        // No data is present. Need to make an API request.
        this.fetchTestResults();
      }
    },
    hitEnterClear: function() {
      // Do nothing unless the full command is written.
      if (this.clear_prompt_text != clear_target) return;

      // Reset the display, hiding the now-cached results.
      // This emulates the "clear" command in a unix terminal.
      this.hide_results = true;
      this.can_clear = false;
      this.is_error = false;
      this.main_prompt_text = "";
      this.clear_prompt_text = "";
      this.$refs.main_input.focus(); // Reset the cursor as well.
    },
    fetchTestResults: function() {
      const self = this;

      const start_time = Date.now();
      getTestResults()
        .then(function(response) {
          const is_okay = response.data && typeof response.data == "string";
          self.is_error = !is_okay;

          if (is_okay) {
            self.results = response.data.split("\n");
            self.hide_results = true;
            console.log(self.results);
          }
        })
        .catch(function(error) {
          // Triggers a network error message in the terminal UI.
          self.is_error = true;
          console.log(error);
        })
        .then(function() {
          // The API request took some time.
          // No need to emulate the full delay for testing.
          const target_duration = calcDuration(self.results);
          const elapsed = Date.now() - start_time;
          self.showTestResultsCached(target_duration, elapsed);
        });
    },
    updateInputMain: function(event) {
      // The main_prompt_text field is bound to the input tags content.
      // Clearing the value ensures that the actual input is ignored.
      // The calcUpdatedText method adds or subtracts the correct letter.
      // Addition/subtraction is determined by the event.inputType field.
      const previous = this.main_prompt_text;
      this.main_prompt_text = "";
      this.main_prompt_text = calcUpdatedText(
        previous,
        main_target,
        event.inputType
      );
    },
    updateInputClear: function(event) {
      // See updateInputMain.
      const previous = this.clear_prompt_text;
      this.clear_prompt_text = "";
      this.clear_prompt_text = calcUpdatedText(
        previous,
        clear_target,
        event.inputType
      );
    },
    startTrackingMouse: function(event) {
      // Used to differentiate longer mouse gestures from basic clicks.
      this.last_mouse_event = event.timeStamp;
    },
    handleTerminalClick: function(event) {
      // Ignore mouse gestures such as long-press or click+drag.
      const duration = event.timeStamp - this.last_mouse_event;
      if (this.last_mouse_event > 0 && duration > drag_duration) return;

      if (this.can_clear) {
        this.$refs.clear_input.focus();
      } else {
        this.$refs.main_input.focus();
      }
    }
  }
};
</script>

<style>
#term-window {
  background: #282828;
  padding: 6px;
  min-height: 36rem;
}

#term-window p span,
#term-window pre,
#term-error,
.term-entry,
.term-text {
  font-size: 1.125rem;
  text-align: left;
  font-family: "Lucida Console", "Courier New", Monaco, monospace;
  margin: unset;
  max-lines: 2;
}

#term-window p {
  text-align: left;
}

.term-prompt {
  color: #f8f8f8;
  align-self: center;
}

.term-entry {
  background: #282828;
  color: #b8b8b8;
  border-style: none;
  outline: none;
}

.term-entry:focus {
  border-style: none;
  outline: none;
}

#term-error {
  color: #fa8f87;
}

#term-loc {
  color: #779ae6;
}

#term-branch {
  color: #93cc6a;
}

.term-text {
  color: #b8b8b8;
  word-wrap: break-word;
  word-break: break-all;
}

pre.term-text {
  overflow-x: auto;
  white-space: pre-wrap;
  white-space: -moz-pre-wrap;
  white-space: -pre-wrap;
  white-space: -o-pre-wrap;
}

pre.term-text:empty::after {
  content: "&nbsp;";
  visibility: hidden;
}
</style>
