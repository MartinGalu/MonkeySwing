import { CredentialResponse } from "@react-oauth/google";
import { useMutation, useQuery } from "react-query";
import { getMe, login } from "src/api/auth";
import { Credentials } from "src/types/credentials";
import { User } from "src/types/user";


export function useLogin() {
    return useMutation<void, Error, CredentialResponse>(async creds => login(creds));
}
  
export const useGetMe = () => {
    return useQuery<User, Error>(['user', 'me'], async () => {
        return getMe();
    });
}