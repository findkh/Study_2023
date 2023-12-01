<template>
    <div v-bind:style="[baseStyle, addStyle]">인라인 스타일 바인딩</div>
</template>

<script>
export default {
    data() {
        return {
            baseStyle : 'background-color:yellow;width:100%;height:200px;',
            addStyle : 'color:red;font-weight:bold;'
        }
    }
}
</script>
