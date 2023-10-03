import { dayjs } from 'src/utils/dayjs';
import { client } from 'src/utils/client';
import { queryClient } from 'src/config';
import { User } from 'src/types/user';
import { decodeJwt } from 'jose';
import { CredentialResponse } from '@react-oauth/google';

export const LOCAL_STORAGE_KEY = '__backoffice_login_data__';

export async function login(login: CredentialResponse) {
const jwt = login.credential;
    if(jwt) {
        const claims = decodeJwt(jwt);
        const { email, name, picture } = claims;
        const user = {
            email,
            name,
            picture,
        } as User;
        saveLoginDataToLocalStorage(user);

        console.log(user);   
    }
}

export function logout() {
  clearLoginDataFromLocalStorage();
  queryClient.clear();
}

export async function getMe(): Promise<User> {
  const loginData = getLoginDataFromLocalStorage();
  if (!loginData) {
    throw new Error('Not authenticated');
  }
  return loginData;
}

export function saveLoginDataToLocalStorage(data: User) {
  localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(data));
}

export function clearLoginDataFromLocalStorage() {
  localStorage.removeItem(LOCAL_STORAGE_KEY);
}

export function getLoginDataFromLocalStorage(): User | undefined {
  try {
    const dataString = localStorage.getItem(LOCAL_STORAGE_KEY);
    if (!dataString) return undefined;
    return JSON.parse(dataString);
  } catch (error) {
    throw new Error('Unable to parse user data from local storage: ' + error);
  }
}
