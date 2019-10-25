<template>
  <div v-if="this.user==='Administrador'"></div>
  <div v-else-if="this.user==='Medico'"></div>
  <div v-else-if="this.user==='Hospital'"></div>
  <div v-else-if="this.user==='Civil'"></div>
</template>