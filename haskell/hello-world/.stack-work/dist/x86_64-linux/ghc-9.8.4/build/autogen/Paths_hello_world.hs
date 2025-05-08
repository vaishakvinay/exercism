{-# LANGUAGE CPP #-}
{-# LANGUAGE NoRebindableSyntax #-}
#if __GLASGOW_HASKELL__ >= 810
{-# OPTIONS_GHC -Wno-prepositive-qualified-module #-}
#endif
{-# OPTIONS_GHC -fno-warn-missing-import-lists #-}
{-# OPTIONS_GHC -w #-}
module Paths_hello_world (
    version,
    getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir,
    getDataFileName, getSysconfDir
  ) where


import qualified Control.Exception as Exception
import qualified Data.List as List
import Data.Version (Version(..))
import System.Environment (getEnv)
import Prelude


#if defined(VERSION_base)

#if MIN_VERSION_base(4,0,0)
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#else
catchIO :: IO a -> (Exception.Exception -> IO a) -> IO a
#endif

#else
catchIO :: IO a -> (Exception.IOException -> IO a) -> IO a
#endif
catchIO = Exception.catch

version :: Version
version = Version [1,1,0,5] []

getDataFileName :: FilePath -> IO FilePath
getDataFileName name = do
  dir <- getDataDir
  return (dir `joinFileName` name)

getBinDir, getLibDir, getDynLibDir, getDataDir, getLibexecDir, getSysconfDir :: IO FilePath




bindir, libdir, dynlibdir, datadir, libexecdir, sysconfdir :: FilePath
bindir     = "/home/vaishak/exercism/haskell/.stack-work/install/x86_64-linux/b8ba322b2673532d229eb3e898a62bc3b25e2ace82def43a3bc6237dcef92cae/9.8.4/bin"
libdir     = "/home/vaishak/exercism/haskell/.stack-work/install/x86_64-linux/b8ba322b2673532d229eb3e898a62bc3b25e2ace82def43a3bc6237dcef92cae/9.8.4/lib/x86_64-linux-ghc-9.8.4/hello-world-1.1.0.5-IRx9086RdVd2Vs63UlpAeJ"
dynlibdir  = "/home/vaishak/exercism/haskell/.stack-work/install/x86_64-linux/b8ba322b2673532d229eb3e898a62bc3b25e2ace82def43a3bc6237dcef92cae/9.8.4/lib/x86_64-linux-ghc-9.8.4"
datadir    = "/home/vaishak/exercism/haskell/.stack-work/install/x86_64-linux/b8ba322b2673532d229eb3e898a62bc3b25e2ace82def43a3bc6237dcef92cae/9.8.4/share/x86_64-linux-ghc-9.8.4/hello-world-1.1.0.5"
libexecdir = "/home/vaishak/exercism/haskell/.stack-work/install/x86_64-linux/b8ba322b2673532d229eb3e898a62bc3b25e2ace82def43a3bc6237dcef92cae/9.8.4/libexec/x86_64-linux-ghc-9.8.4/hello-world-1.1.0.5"
sysconfdir = "/home/vaishak/exercism/haskell/.stack-work/install/x86_64-linux/b8ba322b2673532d229eb3e898a62bc3b25e2ace82def43a3bc6237dcef92cae/9.8.4/etc"

getBinDir     = catchIO (getEnv "hello_world_bindir")     (\_ -> return bindir)
getLibDir     = catchIO (getEnv "hello_world_libdir")     (\_ -> return libdir)
getDynLibDir  = catchIO (getEnv "hello_world_dynlibdir")  (\_ -> return dynlibdir)
getDataDir    = catchIO (getEnv "hello_world_datadir")    (\_ -> return datadir)
getLibexecDir = catchIO (getEnv "hello_world_libexecdir") (\_ -> return libexecdir)
getSysconfDir = catchIO (getEnv "hello_world_sysconfdir") (\_ -> return sysconfdir)



joinFileName :: String -> String -> FilePath
joinFileName ""  fname = fname
joinFileName "." fname = fname
joinFileName dir ""    = dir
joinFileName dir fname
  | isPathSeparator (List.last dir) = dir ++ fname
  | otherwise                       = dir ++ pathSeparator : fname

pathSeparator :: Char
pathSeparator = '/'

isPathSeparator :: Char -> Bool
isPathSeparator c = c == '/'
