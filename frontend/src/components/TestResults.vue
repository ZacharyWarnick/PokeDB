<template>
  <b-container>
    <b-row>
      <b-col>
        <b-button v-on:click="fetchTestResults" variant="outline-secondary">
          Run Unit Tests</b-button
        >
      </b-col>
    </b-row>
    <div id="term-window" v-on:click="showClick">
      <p>
        <span id="term-loc">pikachu@pokedex:~/cs329-idb </span
        ><span id="term-branch">(master)</span>
      </p>
      <p>
        <span class="term-prompt"
          >&#9656;&nbsp;<input
            class="term-input"
            id="main-input"
            ref="main_input"
            :value="main_prompt_text"
            v-on:input="updateMainInput"
            @keydown.enter="hitMainEnter"
        /></span>
      </p>
      <pre
        v-show="!hide_results"
        v-for="(line, index) in results"
        :key="index"
        class="term-text"
        >{{ line }}</pre
      >
      <p v-show="can_clear">
        <span class="term-prompt"
          >&#9656;&nbsp;<input
            class="term-input"
            id="clear-input"
            ref="clear_input"
            :value="clear_prompt_text"
            v-on:input="updateClearInput"
            @keydown.enter="hitClearEnter"
        /></span>
      </p>
    </div>
  </b-container>
</template>

<script>
import { getTestResults } from "@/api";

const getUpdatedText = function(current, target, event_type) {
  if (event_type == "deleteContentBackward") {
    if (current.length <= 1) {
      return "";
    } else {
      return current.slice(0, current.length - 1);
    }
  } else if (event_type == "insertText") {
    const end_index = current.length + 1;
    if (end_index <= target.length) {
      return target.slice(0, end_index);
    } else {
      return target;
    }
  }

  return current;
};

const clear_target = "clear";
const main_target = "make view-coverage";

export default {
  name: "TestResults",
  data() {
    return {
      main_prompt_text: "",
      clear_prompt_text: "",
      results: [],
      can_clear: false,
      hide_results: false
    };
  },
  methods: {
    hitMainEnter: function() {
      if (this.main_prompt_text.length != main_target.length) {
        return;
      }

      this.hide_results = false;
      this.fetchTestResults();
    },
    hitClearEnter: function() {
      if (this.clear_prompt_text.length != clear_target.length) {
        return;
      }

      this.hide_results = true;
      this.can_clear = false;
      this.main_prompt_text = "";
      this.clear_prompt_text = "";
      this.$refs.main_input.focus();
    },
    fetchTestResults: function() {
      if (this.results.length > 0) {
        this.can_clear = true;
        this.$nextTick(() => {
          this.$refs.clear_input.focus();
        });
        return;
      }

      const self = this;

      getTestResults().then(function(response) {
        if (response.data != null && typeof response.data == "string") {
          self.results = response.data.split("\n");
          self.can_clear = true;
          self.$refs.main_input.blur();

          self.$nextTick(() => {
            self.$refs.clear_input.focus();
          });
        }
      });
    },
    updateMainInput: function(event) {
      const previous = this.main_prompt_text;
      this.main_prompt_text = "";
      this.main_prompt_text = getUpdatedText(
        previous,
        main_target,
        event.inputType
      );
    },
    updateClearInput: function(event) {
      if (!this.can_clear) return;

      const previous = this.clear_prompt_text;
      this.clear_prompt_text = "";
      this.clear_prompt_text = getUpdatedText(
        previous,
        clear_target,
        event.inputType
      );
    },
    showClick: function() {
      console.log(this.$refs);
      this.$refs.main_input.focus();
    }
  }
};
</script>

<style>
#term-window {
  background: #282828;
  padding: 5px;
  min-height: 32rem;
}

#term-window::before {
  max-width: 100%;
}

#term-window pre,
#term-window p span,
#term-window p,
.term-input,
.term-text {
  font-size: 1.125rem;
  text-align: left;
  font-family: "Lucida Console", "Courier New", Monaco, monospace;
  margin: unset;
  max-lines: 2;
  padding: 0.05rem 0;
}

.term-prompt {
  color: #f8f8f8;
  align-self: center;
}

.term-input {
  background: #282828;
  color: #b8b8b8;
  border-style: none;
  outline: none;
}

#term-input:focus {
  border-style: none;
  outline: none;
}

#term-input:read-only #term-loc {
  color: #7cafc2;
}

#term-branch {
  color: #a1b56c;
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
  word-wrap: break-word;
}
</style>
