<template>
    <div>
        <img v-bind:src="imgSrc" />
    </div>
</template>

<script>
export default {
    data() {
        return {
            imgSrc: "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Vue.png/330px-Vue.png"
        }
    }
}
</script>
