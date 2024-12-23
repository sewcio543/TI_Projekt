export const getCookie = async (name) => {
    const token = document.cookie
        .split("; ")
        .find((row) => row.startsWith(`${name}=`))
        ?.split("=")[1];

    return token;
}