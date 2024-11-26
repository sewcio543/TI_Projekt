export const getCookie = async () => {
    const token = document.cookie
        .split("; ")
        .find((row) => row.startsWith("bearer="))
        ?.split("=")[1];

    console.log("Bearer Token:", token);
    return token;
}