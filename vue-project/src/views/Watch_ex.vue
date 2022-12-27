<template>
    <h1>Full Name; {{ fullName }}</h1>
</template>

<script>
export default {
    data() {
        return {
            firstName : 'Sudal',
            lastName : 'park',
            fullName : ''
        };
    },
    watch: {
        firstname() {
            this.fullName = this.firstName + ' ' + this.lastName;
        },
        lastName() {
            this.fullName = this.firstName + ' ' + this.lastName;
        }
    }
}
</script>

<style>

</style>