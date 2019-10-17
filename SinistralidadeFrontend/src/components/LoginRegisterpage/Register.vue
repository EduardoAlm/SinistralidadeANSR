<template>
  <div class="w3-container w3-display-middle" style="width: 500px">
    <h1>Register Page</h1>
    <p>&nbsp;</p>
    <div class="component-container" style="width: 40%;
    margin: 0 auto;">
      <h4>Número de cartão de cidadão</h4>
      <input
        :id="nCC"
        v-model="nCC"
        class="w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
        style="border:2px solid grey"
        @keypress="checkNull"
        type="number"
      />
      <p>&nbsp;</p>
      <h4>Nome de Utilizador</h4>
      <input
        :id="userName"
        v-model="userName"
        class="w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
        style="border:2px solid grey"
        type="text"
        @keypress="checkNull"
      />
      <div v-if="checkFlagCN">
        <label
          class="w3-text-light-green"
          style
        >The contract name corresponds to the inserted address!</label>
      </div>
      <div v-else>
        <label class="w3-text-red" style>Please enter the correct name!</label>
      </div>
      <p>&nbsp;</p>
      <h4>Required Tezos Amount</h4>
      <input
        :id="tzAmount"
        v-model="tzAmount"
        @keypress="checkNull"
        class="w3-input w3-border-5 w3-hover-border-green w3-round-large w3-light-grey"
        style="border:2px solid grey"
        type="text"
        @keyup="checkAmount"
      />
      <label class="w3-text-light-green" style>
        Colateral is 50% of the transaction required amount:
        {{ this.tzAmount * 0.5 }} tz
      </label>
      <div v-if="checkFlagA == true && checkFlagBal == true">
        <label class="w3-text-light-green" style>The required amount is correct!</label>
      </div>
      <div v-else-if="checkFlagBal == false && checkFlagA == true">
        <label class="w3-text-red" style>You dont have enough xtz!</label>
      </div>
      <div v-else>
        <label class="w3-text-red" style>Please enter the required amount!</label>
      </div>
      <p>&nbsp;</p>
      <div
        v-if="
          checkFlagA == false ||
            checkFlagAdd == false ||
            checkFlagCN == false ||
            checkFlagBal == false ||
            createFlag == true
        "
      >
        <button
          class="w3-button w3-round w3-green w3-hover-opacity"
          @click="getInfo"
          disabled
        >Accept Transaction</button>
      </div>
      <div v-else>
        <button
          class="w3-button w3-round w3-green w3-hover-opacity"
          @click="getInfo"
        >Accept Transaction</button>
      </div>
      <div class="alert alert-success" style="margin-top:20px" v-if="createFlag == true">
        <strong>Success!</strong>
        You have successfully submitted the transaction data.
        <strong>To create a new one you have to go to the buyer home page first.</strong>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Register",
  data: function() {
    return {};
  },
  methods: {
    checkNull() {
      if (
        this.sAdd === "" ||
        this.contractName === "" ||
        this.tzAmount === ""
      ) {
        this.nullFlag = true;
      } else {
        this.nullFlag = false;
      }
    }
  }
};
</script>
